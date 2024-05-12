import sys
# import bisect
import django
from django.conf import settings
# Configure Django settings
settings.configure(DEBUG=True)
# Initialize Django
django.setup()
sys.path.append("/home/tinsae/Desktop/projects/AHF_Fintech/utils/")
import calc_res


print("sys path ",sys.path)

def function(q22):
    branch_gross = 275000
    total_expense = 20794
    return calc_res.calculate_balance(branch_gross,total_expense,q22)




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