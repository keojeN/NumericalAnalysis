from colors import bcolors
from matrix_utility import *
from gaussian_elimination import gaussianElimination

def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points] # Makes the initial matrix
    b = [[point[1]] for point in table_points]
    for i in range(len(matrix)):
        matrix[i].append(b[i][0])

    print(bcolors.OKBLUE, "The matrix obtained from the points: ", bcolors.ENDC, '\n', np.array(matrix))
    matrixSol = gaussianElimination(matrix)
    print(bcolors.OKBLUE, "\nMat solve:" , matrixSol , bcolors.ENDC)

    result = sum([matrixSol[i] * (x ** i) for i in range(len(matrixSol))])
    print(bcolors.OKBLUE, "\nThe polynom:", bcolors.ENDC)
    print('P(X) = '+'+'.join([ '('+str(matrixSol[i])+') * x^' + str(i) + ' ' for i in range(len(matrixSol))]))
    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC)
    print(result)
    return result

if __name__ == '__main__':
    table_points = [(1.2, -3.50), (1.3,-3.69), (1.4,0.09043), (1.5,1.1293), (1.6,2.3756)]
    x = 1.35
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x,'\n')
    polynomialInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)