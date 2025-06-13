#  Create a 10×10 array with random numbers and find the position of the maximum value.
import numpy as np
arr = np.random.randint(1,100, size=(10,10))
print(arr)

# Find position of maximum value
max_pos = np.unravel_index(np.argmax(arr),arr.shape)
print("Position of max value (row, col):", max_pos)

row, col = max_pos
print("Position of max value (row, col):", (int(row), int(col)))

'''--🔹 1. np.argmax(arr)
This returns the index of the maximum value in the array, but it treats the entire array as a 1D (flattened) array.

🔹 2. np.unravel_index(...)
This function converts a 1D index into 2D coordinates (row, col) based on the shape of the array.



🔹 3. arr.shape
This provides the shape of the array (e.g., (10, 10) if it's a 10×10 array).

You pass this to unravel_index so it knows how to convert from flat index to 2D coordinates.--'''