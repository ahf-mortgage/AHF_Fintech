import bisect
from utils.calc_res import calculate_balance,calculate_gross__new_branch_income,calculate_total_expense,calculate_above_loan_break_point_ahf_commission
from recruiter.models import LoanBreakPoint,CompPlan,Branch
from W2branchYearlyGross.models import Q22


loan_break_point = LoanBreakPoint.objects.all().first()
comp_plan        = CompPlan.objects.all().first()
branch           = Branch.objects.all().first()  
gci = 2700





def function(q22):
        branch_gross = calculate_gross__new_branch_income(loan_break_point,comp_plan,gci,branch)
        above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(loan_break_point,comp_plan,branch) #int(flat_fee_gci * (branch.commission))
        total_expense = calculate_total_expense(branch_gross,above_loan_break_point_ahf_commission)
        # branch_gross = 275000
        # total_expense = 20794
        return calculate_balance(branch_gross,total_expense,q22)

def find_root(function, left, right, tolerance):
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
            
            # print("midpoint balance =",function(midpoint),"q22=",midpoint.value)
            # print("left balance     =",function(left),    "q22=",left.value)
            # print("right balance    =",function(right),   "q22=",right.value)
            
            if function(midpoint) == 0 :
                return midpoint
            elif function(midpoint) * function(left) < 0:
                right = midpoint               
            else:
                left = midpoint
            i += 1

        return (_left + _right) / 2

# Define the interval [left, right] and the desired tolerance
# left = 1
# right = 3
# tolerance = 1e-6

# # Find the root using the bisection method
# root = find_root(function, left, right, tolerance)
# print("Root:", root)
# print("Function value at the root:", function(root))