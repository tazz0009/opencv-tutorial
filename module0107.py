import cv2
import matplotlib.pyplot as plt

# Split the image into the B,G,R components
img_NZ_bgr = cv2.imread("assets/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)

# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)

img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)
# Split the image into the B,G,R components
h, s, v = cv2.split(img_hsv)

h_new = h+10
img_NZ_merged = cv2.merge((h_new, s, v))
img_NZ_rgb = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2RGB)

# Show the channels
plt.figure(figsize=[20, 5])
plt.subplot(141)
plt.imshow(h, cmap='gray')
plt.title("H Channel")
plt.subplot(142)
plt.imshow(s, cmap='gray')
plt.title("S Channel")
plt.subplot(143)
plt.imshow(v, cmap='gray')
plt.title("V Channel")
plt.subplot(144)
plt.imshow(img_NZ_rgb)
plt.title("Original")

plt.imshow(img_NZ_rgb)
plt.show()
