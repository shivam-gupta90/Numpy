from PIL import Image
import numpy as np

# Step 1: Load the image
image_path = "/Applications/code/Numpy/project/00E07B99-BA35-4957-BE8B-C7E8BF128327.jpeg"  # Replace with your image path
img = Image.open(image_path)

# Step 2: Convert image to NumPy array
img_array = np.array(img)

# Step 3: Check if image has RGB channels
if img_array.ndim == 3 and img_array.shape[2] == 3:
    # Step 4: Extract RGB channels
    R = img_array[:, :, 0]
    G = img_array[:, :, 1]
    B = img_array[:, :, 2]

    # Step 5: Apply grayscale conversion formula
    gray_array = 0.2989 * R + 0.5870 * G + 0.1140 * B
    gray_array = gray_array.astype(np.uint8)  # Convert to 8-bit integer format

    # Step 6: Convert NumPy array back to image
    gray_img = Image.fromarray(gray_array)

    # Step 7: Save and show the grayscale image
    gray_img.save("grayscale_output.jpg")
    gray_img.show()
else:
    print("The image is not in RGB format.")
