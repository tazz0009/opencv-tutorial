import cv2

# Loading image
img = cv2.imread('assets/tazz001.jpg', 1)
# -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image
# 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

# resize
img = cv2.resize(img, (0, 0), fx=2, fy=2)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# Write image
cv2.imwrite('tazz001_rotated.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
