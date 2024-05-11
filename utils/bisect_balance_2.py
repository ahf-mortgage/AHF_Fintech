import bisect
import calc_res
# from recruiter.models import *

# def function(x):
#     # The function for which you want to find the root
#     return x**3 - 2*x - 5

def function(q22):
    branch_gross = 275000
    total_expense = 20794
    return calculate_balance(branch_gross,total_expense,q22)

# def function(self,q22):
#         # self.branch_gross = calculate_gross__new_branch_income(self.loan_break_point,self.comp_plan,self.gci,self.branch)
#         # self.above_loan_break_point_ahf_commission = calculate_above_loan_break_point_ahf_commission(self.loan_break_point,self.comp_plan,self.branch) #int(flat_fee_gci * (branch.commission))
#         # self.total_expense = calculate_total_expense(self.branch_gross,self.above_loan_break_point_ahf_commission)
        
#         branch_gross = 275000
#         total_expense = 20794
#         return calculate_balance(branch_gross,total_expense,self.q22)


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
left = 1
right = 3
tolerance = 1e-6

# Find the root using the bisection method
root = find_root(function, left, right, tolerance)
print("Root:", root)
print("Function value at the root:", function(root))