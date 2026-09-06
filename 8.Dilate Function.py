import cv2
import numpy as np

# Read the image
img = cv2.imread("sample.jpg")

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(img, kernel, iterations=1)

# Display original and dilated images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
