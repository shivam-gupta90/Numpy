#2. Create a 3×3 matrix with all True values.
import numpy as np
matrix = np.ones((3,3),dtype=bool)
print(matrix)

'''We use **np.ones()** to create an array filled with 1s. But in your case, 
we want a 3×3 matrix filled with True values, not numeric 1s.

Why np.ones((3, 3), dtype=bool) gives True:
When you use dtype=bool, NumPy converts the value 1 into True.

So, np.ones() makes a matrix of 1s → then dtype=bool converts those 1s into True.'''