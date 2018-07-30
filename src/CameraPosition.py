import cv2
import numpy as np
import csv
from Point2d import Point2d
import GetMatrix
points1 = []
points2 = []
with open('C:/Users/nianq/OneDrive/Documents/GitHub/MonmouthSRPImage/src/project_files/24.JPG_14.JPG_matches.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         points1.append(row[2:4])
         points2.append(row[0:2])

points2.pop(0)
points1.pop(0)

# Example. Estimation of fundamental matrix using the RANSAC algorithm

#find the camera matrix

mtx = GetMatrix.cameraMatrix
mtx = np.array(mtx,dtype = np.float32)

points1 = np.array(points1,dtype = np.float32)
points2 = np.array(points2,dtype = np.float32)

pictureWL = (3000,4000)


#find the essential matrix using the results of the fundamental matrix
# K must be found before hand
essential_matrix, mask = cv2.findEssentialMat(points1, points2, 3.61, pictureWL,8, 0.99, 1.0)

#Derive R and Tx from the u, s, and v

rotation = cv2.recoverPose(essential_matrix, points1, points2, mtx,3.61,mask)

R = cv2.Rodrigues(rotation[1])
translation = cv2.Rodrigues(rotation[2])

R = np.array(R[0]).transpose()
t = np.matmul(-1*R, translation[0])
print t

'''
fundamental_matrix = findFundamentalMat(points1, points2, FM_RANSAC, 3, 0.99)
#Compute the Singular Value Decomposition of E
#u, s, vh = np.linalg.svd(essential_matrix, full_matrices=True)


#Retrieve camera position 
Rodrigues(rotation, R)
R = zip(*R)
t = -R * translation
'''

