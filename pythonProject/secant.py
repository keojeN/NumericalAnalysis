import math
def secant_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds all roots of a function f within a range (a, b) using the Secant method.

    Args:
        f: The function for which to find roots.
        a: Lower bound of the range.
        b: Upper bound of the range.
        tol: Tolerance for convergence (default: 1e-4).
        max_iter: Maximum number of iterations (default: 100).

    Returns:
        A list of tuples containing root and number of iterations for each root found within the range (a, b).
    """
    roots = []
    already_found = set()  # Set to keep track of roots already found
    for x0 in range(a, b):
        x0 = float(x0)
        x1 = x0 + 1  # Initial guess for the second point

        # Check if function value is close to zero at the current point
        if abs(f(x0)) < tol:
            rounded_x0 = round(x0, 5)
            if a < rounded_x0 < b:
             if rounded_x0 not in already_found:  # Check if root has already been found
                 roots.append((rounded_x0, 0))  # Append root and 0 iterations
                 already_found.add(rounded_x0)
            continue

        # Secant method iteration
        for iterations in range(1, max_iter + 1):
            if abs(x1 - x0) < tol:
                rounded_x1 = round(x1, 5)
                if a < rounded_x1 < b:
                    if rounded_x1 not in already_found:  # Check if root has already been found
                        roots.append((rounded_x1, iterations))  # Append root and iterations
                        already_found.add(rounded_x1)
                break

            if ((f(x1) - f(x0)) == 0):
                continue

            # Compute next approximation
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))


            # Update points for the next iteration
            x0, x1 = x1, x2

    return roots

# Example usage (replace f with your actual function)
def f(x):
    return x**2-3*x*math.sin(x)


roots = secant_method(f, -3, 5)
print("Roots and Iterations:")
for root, iterations in roots:
    print("Root:", root, "| Iterations:", iterations)
