# Find common values between two arrays.
import numpy as np
arr = np.array([1,2,3,4,5])
arr1 = np.array([8,9,3,2,10])

# Find common elements
common = np.intersect1d(arr, arr1)
print(common)