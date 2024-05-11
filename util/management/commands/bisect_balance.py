import bisect
from util.calc_res import calculate_balance,calculate_gross__new_branch_income,calculate_total_expense,calculate_above_loan_break_point_ahf_commission
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
    
    print("xxxxxxxxxxxxxxxxxxxxxxxbranch_gross=",branch_gross)
    print("xxxxxxxxxxxxxxxxxxxxxxxtotal_expense=",total_expense)
    print("xxxxxxxxxxxxxxxxxxxxxxxq22=",q22.value)
    
    return calculate_balance(branch_gross,total_expense,q22)

def find_root(function, left, right, tolerance):
    # Bisection method to find the root of a function
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

# Define the interval [left, right] and the desired tolerance
q22 = Q22.objects.all().first()
q22.value = 0
left = q22
q22.value = 100
right = q22
tolerance = 1e-6

# Find the root using the bisection method
root = find_root(function, left, right, tolerance)
print("Root:", root)
print("Function value at the root:", function(root))