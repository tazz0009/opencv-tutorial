import cv2
import matplotlib.pyplot as plt

# Split the image into the B,G,R components
img_NZ_bgr = cv2.imread("assets/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)

# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(img_NZ_rgb)
plt.show()
