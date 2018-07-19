import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/14.JPG',0)          # queryImage
img2 = cv2.imread('/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/24.JPG',0) # trainImage

# Initiate SIFT detector
surf = cv2.xfeatures2d.SURF_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    print(str(m)," ",str(n))
    if m.distance < 0.75*n.distance:
        good.append([m])
# Initialize lists
list_kp1 = []
list_kp2 = []
print(len(good))
'''
# For each match...
for mat in good:
    
    # Get the matching keypoints for each of the images
    img1_idx = mat[0].queryIdx
    img2_idx = mat[0].trainIdx
    
    # x - columns
    # y - rows
    # Get the coordinates
    (x1,y1) = kp1[img1_idx].pt
    (x2,y2) = kp2[img2_idx].pt
    
    # Append to each list
    list_kp1.append((x1, y1))
    list_kp2.append((x2, y2))
    
print (list_kp1, list_kp2)
'''
# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
plt.imshow(img3)
plt.show()
