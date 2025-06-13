import numpy as np
from scipy.signal import convolve2d
from PIL import Image
import matplotlib.pyplot as plt

# Load image and convert to grayscale
img = Image.open("/Applications/code/Numpy/project/project03/sample.jpg").convert("L")  # L mode = grayscale
image_array = np.array(img)

# Define a sharpening kernel
sharpen_kernel = np.array([[ 0, -1,  0],
                           [-1,  5, -1],
                           [ 0, -1,  0]])

# Apply convolution
filtered_image = convolve2d(image_array, sharpen_kernel, mode='same', boundary='symm')

# Plot original and filtered image side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_array, cmap='gray')
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Filtered (Sharpened)")
plt.imshow(filtered_image, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.show()
