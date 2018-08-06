from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
import time

# creating the images list
index = {}
start = time.time()
w, h = 170, 170
Matrix = [[1 for x in range(w)] for y in range(h)]


def compare(pictures, hist, method):
    d = cv2.compareHist(pictures, hist, method)
    return d


# set the image paths
dataset = "C:/Users/nianq/Desktop/image recog/compare-histograms-opencv/TrainTracks/"
# loop over the image paths
count = 0
for imagePath in glob.glob(dataset + "/*.JPG"):
    # extract the image filename (assumed to be unique) and
    # load the image, updating the images dictionary
    filename = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    # extract a 3D RGB color histogram from the image,
    # using 8 bins per channel, normalize, and update
    # the index
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
                        [0, 256, 0, 256, 0, 256])

    index[count] = hist
    count = count + 1
    print "reading " + filename



print "finished input using " + str(start - time.time())
# setting the methods
OPENCV_METHODS = (
    ("Correlation", cv2.HISTCMP_CORREL),  # need > 0.8
    ("Chi-Squared", cv2.HISTCMP_CHISQR),  # need < 5000000
    ("Intersection", cv2.HISTCMP_INTERSECT),  # need > 8000000
    ("Hellinger", cv2.HISTCMP_BHATTACHARYYA))  # need <0.3

for (k, hist) in index.items():
    for i in range(k, w - 1, 1):
        # compute the distance between the two histograms
        # using the method and update the results dictionary
        result = compare(index[i], hist, cv2.HISTCMP_CORREL)
        Matrix[i][k] = result
        Matrix[k][i] = result


'''
flag = np.arange(170)
for i in range(0, w - 1, 1):
    group = []
    for j in range(0, w - 1, 1):
        # print "for picture " + str(i) + "and" + str(j) + str (Matrix [i][j])
        if (Matrix[i][j] > 0.8 and flag[j] != -1):
            group.append(j)
    print group
print "finished all using " + str(start - time.time())
'''