# 5. Reverse a 1D array (e.g., [1, 2, 3])
import numpy as np

var = np.array([[1,2,3],[1,2,3]])
print(var)
print(var.ndim)

var1 = var.reshape(-1)
print(var1)
print(var1.ndim)

'''-- in this problem first we make a 2D matrix of array
       after that i print his dimaension by usinf ndim
       .the i use reshape(-1). here -1 is used to convert the 2D to 1D--'''