# --- Image Translation ---

# Define the translation matrix
# T is a 2x3 matrix where:
# T = [[1, 0, tx],
#      [0, 1, ty]]
# tx is the translation amount in the x-direction
# ty is the translation amount in the y-direction
tx = 100  # Translate 100 pixels to the right
ty = 50   # Translate 50 pixels down
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the affine transformation to translate the image
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Display the translated image
print("\nTranslated Image:")
cv2_imshow(translated_image)
