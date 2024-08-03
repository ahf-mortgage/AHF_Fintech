import bisect
from utils.calc_res import calculate_balance,calculate_gross__new_branch_income,calculate_total_expense,calculate_above_loan_break_point_ahf_commission,calculate_debit
from apps.recruiter.models import LoanBreakPoint,CompPlan,Branch
from apps.W2branchYearlyGross.models import Q22
from utils.formatter import logger


loan_break_point = LoanBreakPoint.objects.all().first()
comp_plan        = CompPlan.objects.all().first()
branch           = Branch.objects.all().first()  
gci              = (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  + comp_plan.Flat_Fee




branch_gross                          = calculate_gross__new_branch_income(loan_break_point,comp_plan,gci,branch)

above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(loan_break_point,comp_plan,branch) #int(flat_fee_gci * (branch.commission))
total_expense                         = calculate_total_expense(branch_gross,above_loan_break_point_ahf_commission)


def function(q22):
        branch_gross                          = calculate_gross__new_branch_income(loan_break_point,comp_plan,gci,branch)
        above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(loan_break_point,comp_plan,branch) #int(flat_fee_gci * (branch.commission))
        total_expense                         = calculate_total_expense(branch_gross,above_loan_break_point_ahf_commission)
        return calculate_balance(branch_gross,total_expense,q22)


credit    = calculate_gross__new_branch_income(loan_break_point,comp_plan,gci,branch)


def find_root(function, left, right, tolerance):
        debit     = None
        if function(left) * function(right) >= 0:
            raise ValueError("Root not found in the given interval.")
        
        _left = left.value if left != None else 0
        _right = right.value
        midpoint = None
        while abs(_right - _left) > tolerance:
        
            _left = left.value if left != None else 0
            _right = right.value
            _midpoint = (_left + _right) / 2
            midpoint  = Q22(value = _midpoint)
            right     = Q22(value = _right)
            left      = Q22(value = _left)
            debit = calculate_debit(branch_gross,total_expense,Q22(value = _left + _right /2))

            
            if function(midpoint) == 0 :
                return midpoint
            elif function(midpoint) * function(left) < 0:
                right = midpoint               
            else:
                left = midpoint
        balance = function(midpoint)
        return balance,( _left + _right )/ 2
    

