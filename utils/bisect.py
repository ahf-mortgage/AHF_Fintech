import bisect

def function(x):
    # The function for which you want to find the root
    return x**3 - 2*x - 5

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