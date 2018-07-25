import cv2
import numpy as np
import csv
from Point2d import Point2d
points1 = []
points2 = []
with open('C:/Users/nianq/OneDrive/Documents/GitHub/MonmouthSRPImage/src/project_files/24.JPG_14.JPG_matches.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         points1.append(row[0:1])
         points2.append(row[1:2])

points2.pop(0)
points1.pop(0)

# Example. Estimation of fundamental matrix using the RANSAC algorithm

#find the camera matrix
import GetMatrix
mtx = GetMatrix.cameraMatrix
print(mtx[0][2])
points1 = np.array(points1,dtype = np.float32)
points2 = np.array(points2,dtype = np.float32)

pictureWL = Point2d(2000,3000)

print type(points1[0][0])
#find the essential matrix using the results of the fundamental matrix
# K must be found before hand
essential_matrix = cv2.findEssentialMat(points1, points2, 3.61, pictureWL,8, 0.99, 1.0)
print essential_matrix

'''
fundamental_matrix = findFundamentalMat(points1, points2, FM_RANSAC, 3, 0.99)
#Compute the Singular Value Decomposition of E
#u, s, vh = np.linalg.svd(essential_matrix, full_matrices=True)


#Derive R and Tx from the u, s, and vh
recoverPose(E, points1, points2, mtx, rotation, translation, mask)

#Retrieve camera position 
Rodrigues(rotation, R)
R = zip(*R)
t = -R * translation
'''

