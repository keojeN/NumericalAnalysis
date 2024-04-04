import math
import sympy as sp
'''
" Group: Daniel Houri , 209445071 \n"
     "Yakov Shtefan , 208060111 \n"
     "Eve Hackmon , 209295914 \n"
     "Name: Vladislav Rabinovich 323602383 \n")
'''
def newton_raphson(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds all roots of a function f within a range (a, b) using Newton-Raphson method.

    Args:
        f: The function for which to find roots.
        a: Lower bound of the range.
        b: Upper bound of the range.
        tol: Tolerance for convergence (default: 1e-6).
        max_iter: Maximum number of iterations (default: 100).

    Returns:
        A list of tuples containing root and number of iterations for each root found within the range (a, b).
    """
    def df(x):
        # Approximate derivative using central difference method
        h = 1e-6
        return (f(x + h) - f(x - h)) / (2 * h)

    roots = []
    already_found = set()  # Set to keep track of roots already found
    for x in range(a, b):
        x0 = float(x)
        iterations = 0  # Initialize iterations counter

        # Check if function value is close to zero at the current point
        if abs(f(x0)) < tol:
            rounded_x0 = round(x0,5)
            if (rounded_x1 > a and rounded_x1 < b):
             if rounded_x0 not in already_found:  # Check if root has already been found
                roots.append((rounded_x0, iterations))  # Append root and iterations
                already_found.add(rounded_x0)
            continue

        # Avoid division by zero
        if abs(df(x0)) < tol:
            continue

        # Newton-Raphson iteration
        for _ in range(max_iter):
            x1 = x0 - f(x0) / df(x0)
            iterations += 1  # Increment iterations counter
            if abs(x1 - x0) < tol:
                rounded_x1 = round(x1,5)
                if(rounded_x1>a and rounded_x1<b):
                 if rounded_x1 not in already_found:  # Check if root has already been found
                     roots.append((rounded_x1, iterations))  # Append root and iterations
                     already_found.add(rounded_x1)
                break
            x0 = x1

    return roots

# Example usage (replace f with your actual function)
def f(x):
    return x**2-3*x*math.sin(x)


roots = newton_raphson(f, -3, 5)
print("Roots and Iterations:")
for root, iterations in roots:
    print("Root:", root, "| Iterations:", iterations)
