# Q.1) Using scipy library, perform following linear algebraic operations:
# 1. Solve the system of linear equations:
# a. 9x + 6y – 5z + 2w = 17
# b. 4x + 5y – 7z + 3w = 10
# c. -3x - 4y + 2z - 5w = 20
# d. 6x + y + 9z - w = 23                        


"""
import numpy as np
from scipy.linalg import solve

# Coefficient matrix
A = np.array([[9, 6, -5, 2], [4, 5, -7, 3], [-3, -4, 2, -5], [6, 1, 9, -1]])

# Constants matrix
B = np.array([17, 10, 20, 23])

# Solving the system of equations
X = solve(A, B)

print("The solution of the system of linear equations is:")
print("x =", X[0])
print("y =", X[1])
print("z =", X[2])
print("w =", X[3])
"""




# Q.2)2. Perform the following operations on a matrix
# 𝐴 = [5 3 2
#      6 9 −3
#      1 7 4 ]
# a. Find Inverse of matrix A.
# b. Find Kronecker product of A with B= [
# 3 −1
# 2 −5]
# c. Find determinant of matrix A



import numpy as np
from scipy.linalg import inv, det, kron

# Matrix A
A = np.array([[5, 3, 2], [6, 9, -3], [1, 7, 4]])

# Matrix B
B = np.array([[3, -1], [2, -5]])

# a. Finding inverse of matrix A
A_inv = inv(A)
print("Inverse of matrix A is:")
print(A_inv)

# b. Finding Kronecker product of A with B
AB_kron = kron(A, B)
print("Kronecker product of A and B is:")
print(AB_kron)

# c. Finding determinant of matrix A
A_det = det(A)
print("Determinant of matrix A is:")
print(A_det)

