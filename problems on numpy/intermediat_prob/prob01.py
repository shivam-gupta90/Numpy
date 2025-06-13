#  Reshape a 1D array of 16 elements into a 4×4 matrix.
import numpy as np

matrix = np.arange(1,17)
print(matrix)

matrix1 = matrix.reshape(4,4)
print(matrix1)