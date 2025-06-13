#  Replace NaN values in an array with the column mean.
import numpy as np

# Create array with NaN values
arr = np.array([[1, 2, np.nan],
                [4, np.nan, 6],
                [7, 8, 9]])

# Step 1: Compute column-wise means, ignoring NaNs
col_mean = np.nanmean(arr, axis=0)

# Step 2: Find indices where NaNs are located
inds = np.where(np.isnan(arr))

# Step 3: Replace NaNs with corresponding column mean
arr[inds] = np.take(col_mean, inds[1])

print("Array after replacing NaNs with column mean:\n", arr)
