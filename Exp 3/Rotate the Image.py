import cv2
import numpy as np
import glob
from google.colab.patches import cv2_imshow
from google.colab import drive

# Mount Google Drive to access images
drive.mount('/content/drive')

# Load the image - using the first image found in the opencvim directory
images = glob.glob('/content/drive/My Drive/opencv/Chess Images/*.jpg')
if images:
    image_path = images[0]
    image = cv2.imread(image_path)

    # Get image dimensions
    height, width = image.shape[:2]

    # --- Option 1: Rotate by a fixed angle (90, 180, 270 degrees) ---
    # Rotate 90 degrees clockwise
    rotated_90_clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

   
    # Get the 2D rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # Apply the affine transformation to rotate the image
    rotated_arbitrary = cv2.warpAffine(image, rotation_matrix, (width, height))

    # Display the rotated images (optional)
    cv2_imshow(image)
    cv2_imshow(rotated_90_clockwise)
  
    # cv2.waitKey(0) # cv2.waitKey is not needed with cv2_imshow
    # cv2.destroyAllWindows() # cv2.destroyAllWindows is not needed with cv2_imshow
else:
    print("No images found in the specified directory.")
