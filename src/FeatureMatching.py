import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/24.JPG',0)
img2 = cv2.imread('/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/14.JPG',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

# Initialize lists
list_kp1 = []
list_kp2 = []

# For each match...
for mat in matches:
    
    # Get the matching keypoints for each of the images
    img1_idx = mat.queryIdx
    img2_idx = mat.trainIdx
    
    # x - columns
    # y - rows
    # Get the coordinates
    (x1,y1) = kp1[img1_idx].pt
    (x2,y2) = kp2[img2_idx].pt
    
    # Append to each list
    list_kp1.append((x1, y1))
    list_kp2.append((x2, y2))


img3 = cv2.drawMatches(img1,kp1,img2,kp2, matches[:50], None, flags=2)

plt.figure(num='ORB')
plt.imshow(img3)
plt.show()
