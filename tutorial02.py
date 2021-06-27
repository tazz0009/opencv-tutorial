import cv2
import random

# Loading image
img = cv2.imread('assets/tazz001.jpg', -1)

# print(img)
# print(type(img))
print(img.shape)

# blue green red
# [0, 0, 0]

# for i in range(50):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(
#             0, 255), random.randint(0, 255)]

tag = img[100:130, 170:190]
img[25:55, 75:95] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
