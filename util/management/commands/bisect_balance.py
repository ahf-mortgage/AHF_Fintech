
from django.core.management.base import BaseCommand
import bisect
from util.calc_res import calculate_balance,calculate_gross__new_branch_income,calculate_total_expense,calculate_above_loan_break_point_ahf_commission
from recruiter.models import LoanBreakPoint,CompPlan,Branch
from W2branchYearlyGross.models import Q22

class Command(BaseCommand):
    """
        management command to run bisect balance from termail
    """
    help = 'Process some data'
    
    def __init__(self):
        self.loan_break_point = LoanBreakPoint.objects.all().first()
        self.comp_plan        = CompPlan.objects.all().first()
        self.branch           = Branch.objects.all().first()  
        self.gci              = 27500
        self.q22              =  Q22.objects.all().first()
        self.tolerance        = 1e-6

    def handle(self, *args, **options):
        left = Q22.objects.create(value=0)
        right = Q22.objects.create(value = 100)
        root = self.find_root(self.function, left, right, self.tolerance)
        return root
      

    def function(self,q22):
        # self.branch_gross = calculate_gross__new_branch_income(self.loan_break_point,self.comp_plan,self.gci,self.branch)
        # self.above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(self.loan_break_point,self.comp_plan,self.branch) #int(flat_fee_gci * (branch.commission))
        # self.total_expense = calculate_total_expense(self.branch_gross,self.above_loan_break_point_ahf_commission)
        
        branch_gross = 275000
        total_expense = 20794
        return calculate_balance(branch_gross,total_expense,self.q22)

    def find_root(self,function, left, right, tolerance):
        
        # Bisection method to find the root of a function
        print(left.value,"=left")
        print(right.value,"=right")
        print("function(left)=",function(left))
        print("function(right)=",function(right))
        
        if function(left) * function(right) >= 0:
            raise ValueError("Root not found in the given interval.")

        while abs(right - left) > tolerance:
          
            midpoint = (left + right) / 2
            if function(midpoint) == 0:
                return midpoint
            elif function(midpoint) * function(left) < 0:
                right = midpoint
            else:
                left = midpoint

        return (left + right) / 2
