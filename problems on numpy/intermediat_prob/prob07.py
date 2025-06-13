#  Extract the diagonal of a matrix.
import numpy as np

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
# Extract the diagonal
diagonal = np.diag(matrix)

print("matrix :",matrix)
print("diagoanal :",diagonal)