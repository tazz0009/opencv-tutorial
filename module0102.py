import cv2
import matplotlib.pyplot as plt

# Read image as gray scale.
# cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
# cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_UNCHANGED or -1: Loads image as such including alpha channel.
cb_img_fuzzy = cv2.imread("assets/checkerboard_fuzzy_18x18.jpg", 0)

# Print the image data (pixel values), element of a 2D numpy array.
# Each pixel value is 8-bits [0,255]
print(cb_img_fuzzy)

# print the size  of image
print("Image size is ", cb_img_fuzzy.shape)

# print data-type of image
print("Data type of image is ", cb_img_fuzzy.dtype)

# plt.imshow(cb_img)
plt.imshow(cb_img_fuzzy, cmap='gray')
plt.show()
