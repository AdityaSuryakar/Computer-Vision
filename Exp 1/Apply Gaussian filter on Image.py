from google.colab import drive
drive.mount('/content/drive')
import cv2
from google.colab.patches import cv2_imshow
import sys # Import sys to exit if image loading fails

# Load an image
image_path = '/content/drive/MyDrive/opencv/color_image.jpg' # Define the image path
image = cv2.imread(image_path)

# Add a check to see if the image was loaded successfully
if image is None:
    sys.exit(f"Error: Could not read the image from {image_path}")


# Apply Gaussian blur with specific sigma values
# A symmetrical blur (sigmaX=3, sigmaY=3 implicitly)
blurred_image_1 = cv2.GaussianBlur(image, (5, 5), 3)

# Anisotropic blur (more blur in X than Y)
blurred_image_2 = cv2.GaussianBlur(image, (5, 5), 5, 1)

# Blur with sigma calculated from kernel size
blurred_image_3 = cv2.GaussianBlur(image, (5, 5), 0)

# Display the images (optional)
cv2_imshow(image)
cv2_imshow(blurred_image_1)
cv2_imshow(blurred_image_2)
cv2_imshow(blurred_image_3)
# cv2.waitKey(0) # waitKey and destroyAllWindows are not needed with cv2_imshow
# cv2.destroyAllWindows()
