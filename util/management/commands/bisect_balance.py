
from django.core.management.base import BaseCommand
import bisect
from util.calc_res import calculate_balance,calculate_gross__new_branch_income,calculate_total_expense,calculate_above_loan_break_point_ahf_commission
from recruiter.models import LoanBreakPoint,CompPlan,Branch
from W2branchYearlyGross.models import Q22
import math

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
        left = Q22.objects.filter(value = 0).first()
        right = Q22.objects.filter(value = 100).first()
        root = self.find_root(self.function,left,right,self.tolerance)
        print(root)
        # return root
      

    def function(self,q22):
        self.branch_gross = calculate_gross__new_branch_income(self.loan_break_point,self.comp_plan,self.gci,self.branch)
        self.above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(self.loan_break_point,self.comp_plan,self.branch) #int(flat_fee_gci * (branch.commission))
        self.total_expense = calculate_total_expense(self.branch_gross,self.above_loan_break_point_ahf_commission)
        # branch_gross = 275000
        # total_expense = 20794
        return calculate_balance(self.branch_gross,self.total_expense,q22)

    def find_root(self,function, left, right, tolerance):
        # Bisection method to find the root of a function       
        if function(left) * function(right) >= 0:
            raise ValueError("Root not found in the given interval.")
        
        
        _left = left.value
        _right = right.value
        i = 0 
        while abs(_right - _left) > tolerance:
            _left = left.value
            _right = right.value
            _midpoint = (_left + _right) / 2
            midpoint  = Q22(value = _midpoint)
            right     = Q22(value = _right)
            left      = Q22(value = _left)
            
            print("midpoint balance =",function(midpoint),"q22=",midpoint.value)
            print("left balance     =",function(left),    "q22=",left.value)
            print("right balance    =",function(right),   "q22=",right.value)
            
            if function(midpoint) == 0.0009355954243801534:
                return midpoint
            elif function(midpoint) * function(left) < 0:
                right = midpoint               
            else:
                left = midpoint
            i += 1

        return (_left + _right) / 2
