import cv2
import numpy as np

import time
import re
from os import listdir
from os.path import isfile, join

def sorted_nicely(name):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(name, key=alphanum_key)

def compare(pictures, hist, method):
    d = cv2.compareHist(pictures, hist, method)
    return d

subjectdir = 'C:/Users/nianq/Desktop/image recog/compare-histograms-opencv/TrainTracks/'
onlyfiles = [f for f in listdir(subjectdir) if isfile(join(subjectdir,f))]
onlyfiles = sorted_nicely(onlyfiles)

histIndex = {}
count = 0
print onlyfiles
for fname in onlyfiles:
    print "getting " + str(count) + "picture"
    image = cv2.imread(subjectdir + fname)
    hist = cv2.calcHist([image], [0,1,2], None, [8,8,8], [0, 256,0, 256,0, 256])
    histIndex[count] = hist

    count = count + 1
weight = len(onlyfiles)
histedData = [[1 for x in range(weight)] for y in range(weight)]

# setting the methods
OPENCV_METHODS = (
    ("Correlation", cv2.HISTCMP_CORREL),  # need > 0.8
    ("Chi-Squared", cv2.HISTCMP_CHISQR),  # need < 5000000
    ("Intersection", cv2.HISTCMP_INTERSECT),  # need > 8000000
    ("Hellinger", cv2.HISTCMP_BHATTACHARYYA))  # need <0.3



for (k, hist) in histIndex.items():
    for i in range(k, weight - 1, 1):
        result = compare(histIndex[i], hist, cv2.HISTCMP_CORREL)
        histedData[i][k] = result
        histedData[k][i] = result






