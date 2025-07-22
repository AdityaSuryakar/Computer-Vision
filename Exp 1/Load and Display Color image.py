#Load and display color image
import cv2 as cv
import sys
from google.colab.patches  import cv2_imshow
import os

image_path = "/content/drive/My Drive/opencv/color_image.jpg"

if not os.path.exists(image_path):
  sys.exit(f"Error: Image file not found at path: {image_path}")

img = cv.imread(image_path)

if img is None:
  sys.exit(f"Error: Could not read image from path: {image_path}")

cv2_imshow(img)
