#  Filter an array to only include values greater than 50
import numpy as np

arr = np.array([10, 55, 32, 77, 49, 90, 20])

# Filter values greater than 50
filtered = arr[arr > 50]

print("Original Array:", arr)
print("Filtered Array (values > 50):", filtered)
