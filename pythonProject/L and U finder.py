import pprint
import scipy
import numpy as np
import scipy.linalg   # SciPy Linear Algebra Library

A = np.array([[1, 4,-3],
             [-2 , 8 , 5],
            [3, 4, 2]])
P, L, U = scipy.linalg.lu(A)
print("L:" , L)
print("U:" , U)
print(np.dot(L,U))