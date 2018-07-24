import cv2
import numpy as np
import csv
points1=[36.1111, 1866.09]
points2=[1521.51, 2394.88]
'''
with open('/Users/mahmoudshabana/Documents/SRP Files/' +
              'MonmouthSRPImage/src/project_files/24.JPG_14.JPG_matches.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         points1.append(','.join(row[:2]))
         points2.append(','.join(row[:-2]))

print (points1,points2)
# Example. Estimation of fundamental matrix using the RANSAC algorithm
pointCount = 100


# initialize the points here ... */
for i in range(0, 100):
    points1.append(
    points2[i] = ...;


Mat fundamental_matrix =
 findFundamentalMat(points1, points2, FM_RANSAC, 3, 0.99)
'''
#find the camera matrix


#find the essential matrix using the results of the fundamental matrix
# K must be found before hand
Mat essential_matrix =
 findEssentialMat(points1, points2, mtx, RANSAC, 0.99, 1)


#Compute the Singular Value Decomposition of E
#u, s, vh = np.linalg.svd(essential_matrix, full_matrices=True)


#Derive R and Tx from the u, s, and vh
Mat rotation, translation, R, t, mask
recoverPose(E, points1, points2, mtx, rotation, translation, mask)

#Retrieve camera position 
Rodrigues(rotation, R)
R = zip(*R)
t = -R * translation
'''
