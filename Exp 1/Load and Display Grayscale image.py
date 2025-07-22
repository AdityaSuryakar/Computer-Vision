from google.colab import drive
drive.mount('/content/drive')

import cv2 as cv
import sys
from google.colab.patches import cv2_imshow
import os # Import the os module

# Attempting to load image directly with the path
image_path = "/content/drive/MyDrive/opencv/greyscale_image.jpg"

# Check if the file exists
if not os.path.exists(image_path):
    sys.exit(f"Error: Image file not found at {image_path}")

img = cv.imread(image_path)

if img is None:
    sys.exit("Could not read the image.")

cv2_imshow(img)
