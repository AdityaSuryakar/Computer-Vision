from google.colab import drive
drive.mount('/content/drive')
import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow
import sys # Import sys to exit if image loading fails

img = cv2.imread('/content/drive/MyDrive/opencv/img1.png')

# Add a check to see if the image was loaded successfully
if img is None:
    sys.exit("Error: Could not read the image. Please check the file path.")

median = cv2.medianBlur(img,3)

# Display original and blurred images using cv2_imshow
cv2_imshow(img)
cv2_imshow(median)
