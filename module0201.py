import cv2
import matplotlib.pyplot as plt

# Read image as gray scale.
cb_img = cv2.imread("assets/checkerboard_18x18.png", 0)

cb_img_copy = cb_img.copy()
cb_img_copy[2, 2] = 200
cb_img_copy[2, 3] = 200
cb_img_copy[3, 2] = 200
cb_img_copy[3, 3] = 200

# Same as above
# cb_img_copy[2:3,2:3] = 200

# Set color map to gray scale for proper rendering.
plt.imshow(cb_img_copy, cmap='gray')
print(cb_img_copy)

plt.show()
