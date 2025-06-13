# . Find the standard deviation of an array
import numpy as np

arr1D = np.array([10,20,30,40,50])

# Standard deviation of 1D array
std_1d = np.std(arr1D)

print("1D Array:", arr1D)
print("Standard Deviation (1D):", std_1d)


print()
print()
#for 2D

import numpy as np

# 2D array
arr2D = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])

# Standard deviation of the whole 2D array
std_all = np.std(arr2D)

# Standard deviation along rows (axis=1)
std_rows = np.std(arr2D, axis=1)

# Standard deviation along columns (axis=0)
std_cols = np.std(arr2D, axis=0)

print("2D Array:\n", arr2D)
print("Standard Deviation (entire array):", std_all)
print("Standard Deviation (row-wise):", std_rows)
print("Standard Deviation (column-wise):", std_cols)

