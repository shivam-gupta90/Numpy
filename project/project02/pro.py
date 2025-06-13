import numpy as np
from scipy.signal import convolve2d

# Simulated 5x5 grayscale image
image = np.array([[10, 10, 10, 10, 10],
                  [10, 50, 50, 50, 10],
                  [10, 50,100, 50, 10],
                  [10, 50, 50, 50, 10],
                  [10, 10, 10, 10, 10]])

# Sharpening kernel
kernel = np.array([[ 0, -1,  0],
                   [-1,  5, -1],
                   [ 0, -1,  0]])

# Convolution
filtered = convolve2d(image, kernel, mode='same', boundary='fill', fillvalue=0)

print("Original Image:\n", image)
print("Filtered Image (Sharpened):\n", filtered)
