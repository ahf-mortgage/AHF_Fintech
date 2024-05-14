import bisect
from utils.calc_res import calculate_balance,calculate_gross__new_branch_income,calculate_total_expense,calculate_above_loan_break_point_ahf_commission
from apps.recruiter.models import LoanBreakPoint,CompPlan,Branch
from apps.W2branchYearlyGross.models import Q22


loan_break_point = LoanBreakPoint.objects.all().first()
comp_plan        = CompPlan.objects.all().first()
branch           = Branch.objects.all().first()  
gci = 2700





def function(q22):
        branch_gross                          = calculate_gross__new_branch_income(loan_break_point,comp_plan,gci,branch)
        above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(loan_break_point,comp_plan,branch) #int(flat_fee_gci * (branch.commission))
        total_expense                         = calculate_total_expense(branch_gross,above_loan_break_point_ahf_commission)
        return calculate_balance(branch_gross,total_expense,q22)

def find_root(function, left, right, tolerance):
        if function(left) * function(right) >= 0:
            raise ValueError("Root not found in the given interval.")
        
        
        _left = left.value
        _right = right.value
    
        while abs(_right - _left) > tolerance:
            _left = left.value
            _right = right.value
            _midpoint = (_left + _right) / 2
            midpoint  = Q22(value = _midpoint)
            right     = Q22(value = _right)
            left      = Q22(value = _left)
            if function(midpoint) == 0 :
                return midpoint
            elif function(midpoint) * function(left) < 0:
                right = midpoint               
            else:
                left = midpoint
        return (_left + _right) / 2

