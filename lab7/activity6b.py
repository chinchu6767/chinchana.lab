import numpy as np

matrix1 = np.random.randint(1, 11, (3, 3))
matrix2 = np.random.randint(1, 11, (3, 3))

subtraction = matrix1 - matrix2

division = matrix1 / matrix2

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Subtraction (Matrix1 - Matrix2):\n", subtraction)
print("Element-wise Division (Matrix1 / Matrix2):\n", division)
