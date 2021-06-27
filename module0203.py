import cv2
import matplotlib.pyplot as plt

img_NZ_bgr = cv2.imread("assets/New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
img_NZ_rgb = img_NZ_bgr[:, :, ::-1]
cropped_region = img_NZ_rgb[200:400, 300:600]

resized_cropped_region_2x = cv2.resize(cropped_region, None, fx=2, fy=2)
plt.imshow(resized_cropped_region_2x)
plt.show()
