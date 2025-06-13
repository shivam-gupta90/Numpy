# Normalize an array (Z-score standardization).
import numpy as np

# Original array
arr = np.array([10, 20, 30, 40, 50])

# Calculate mean and standard deviation
mean = np.mean(arr)
std = np.std(arr)

# Z-score normalization
z_score = (arr - mean) / std

print("Original array:", arr)
print("Z-score normalized array:", z_score)



'''
Z-score standardization in NumPy, you subtract the mean and divide by the standard deviation:


formula is : z = x- meuu/sigma 

Where:


X = original array

μ = mean of array

σ = standard deviation of array
'''
