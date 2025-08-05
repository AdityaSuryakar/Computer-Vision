# --- Image Scaling ---

# Resize the image to half its original size
scaled_half = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Resize the image to double its original size
scaled_double = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Resize the image to a specific size (e.g., 300x200)
scaled_specific = cv2.resize(image, (300, 200), interpolation=cv2.INTER_LINEAR)

# Display the scaled images
print("Original Image:")
cv2_imshow(image)
print("\nScaled to Half:")
cv2_imshow(scaled_half)
print("\nScaled to Double:")
cv2_imshow(scaled_double)
print("\nScaled to Specific Size (300x200):")
cv2_imshow(scaled_specific)
