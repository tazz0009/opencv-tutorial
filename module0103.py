import cv2
import matplotlib.pyplot as plt

# Read in image
# cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
# cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_UNCHANGED or -1: Loads image as such including alpha channel.
coke_img = cv2.imread("assets/coca-cola-logo.png", 1)

# print the size  of image
print("Image size is ", coke_img.shape)

# print data-type of image
print("Data type of image is ", coke_img.dtype)

print("")

# matplotlib RGB format
# OpenCV BGR format
coke_img_channels_reversed = coke_img[:, :, ::-1]

# plt.imshow(cb_img)
plt.imshow(coke_img_channels_reversed)
plt.show()
