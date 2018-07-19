import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/24.JPG',0)
img2 = cv2.imread('/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/29.JPG',0)

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


imgORB = cv2.drawMatches(img1,kp1,img2,kp2, matches[:50], None, flags=2)


# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# Initialize lists
list_kp1 = []
list_kp2 = []
print(len(good))
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

# cv2.drawMatchesKnn expects list of lists as matches.
imgSIFT = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
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
imgSURF = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)

pltORB = plt.subplot2grid((3,1),(0,0),rowspan = 1,colspan = 1)
pltSIFT = plt.subplot2grid((3,1),(1,0),rowspan = 1,colspan = 1)
pltSURF = plt.subplot2grid((3,1),(2,0),rowspan = 1,colspan = 1)

pltORB.imshow(imgORB)
pltSIFT.imshow(imgSIFT)
pltSURF.imshow(imgSURF)
plt.show()
