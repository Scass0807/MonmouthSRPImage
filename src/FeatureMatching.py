import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('/Users/Steven/Desktop/Projects/SRP/TrainTracks/outlines/1c78524d-a38c-45bd-b9ff-63b5b1839b33.JPG')
img2 = cv2.imread('/Users/Steven/Desktop/Projects/SRP/TrainTracks/outlines/1f60bf7e-5135-4d93-9c40-46e7bab59c57.JPG')

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2, matches[:20], None, flags=2)
plt.imshow(img3)
plt.show()

