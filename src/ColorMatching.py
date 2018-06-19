## Using OpenCV to match two pictures with color
import cv2
import numpy as np
import csv
from os import listdir
from os.path import isfile, join

## open file for write the data
csvfile = file('csv_test.csv', 'wb')
writer = csv.writer(csvfile)

## have a function for comparing the two pictures
def compare(input1,input2):
    ## open pictures
    img1 = cv2.imread('PATH' + input1)
    img2 = cv2.imread('PATH' + input2)
    
    ## resize the picture from 3000 by 4000 to 300 to 400
    res1 = cv2.resize(img1,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)
    res2 = cv2.resize(img2,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)
    
    ## get the color
    b1,g1,r1 = cv2.split(res1)
    b2,g2,r2 = cv2.split(res2)

    ## variable for calculating the samiliar percent
    percent1 = 0
    count1 = 0
    percent2 = 0
    count2 = 0
    percent3 = 0
    count3 = 0
    
    ## compare the color
    ## samiliar color means the difference bwtween two color is less than 50
    for a in range(0,len(b1)):
        for i in range(0,len(b1[a])):
            x1 = (int) (b1[a][i])
            x2 = (int) (b2[a][i])
            if(abs(x1 - x2) < 50):
                percent1 = percent1 + 1
            count1 = count1 + 1
    for a in range(0,len(g1)):
        for i in range(0,len(g1[a])):
            x1 = (int) (g1[a][i])
            x2 = (int) (g2[a][i])
            if(abs(x1 - x2) < 50):
                percent2 = percent2 + 1
            count2 = count2 + 1
    for a in range(0,len(r1)):
        for i in range(0,len(r1[a])):
            x1 = (int) (r1[a][i])
            x2 = (int) (r2[a][i])
            if(abs(x1 - x2) < 50):
                percent3 = percent3 + 1
            count3 = count3 + 1

    ## get the total percent of the samiliar colors
    totalP = (percent1/float(count1) + percent2/float(count2) + percent3/float(count3))/3

## If the samiliar percent is bigger than 70%, group them in to a floder
##    if totalP > 0.7:
##        cv2.imwrite( "PATH" + input2, img2)

    ## return a list for writing to scv
    return [totalP]

## get the floder path
subjectdir = 'PATH'

## read the picture
onlyfiles = [f for f in listdir(subjectdir) if isfile(join(subjectdir,f))]
writer.writerow([""] + onlyfiles)

## using two for loops to compare all the pictures to each other.
for i in range(0,len(onlyfiles)):
    count = 0
    data = [onlyfiles[i]]
    for fname in onlyfiles:
        print "getting comparing " + str(i) + " picture with " + str(count) + " picture"
        count = count + 1
        data = data + compare(onlyfiles[i],fname)
    writer.writerow(data)
csvfile.close()
## program finished



## testing Open CV

##img1 = cv2.imread(img2)
##img2 = cv2.imread('2.JPG')
###img3 = cv2.imread('3.JPG')
##
###res3 = cv2.resize(img3,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)
###b3,g3,r3 = cv2.split(img3)
##res1 = cv2.resize(img1,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)
##res2 = cv2.resize(img2,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)


#cv2.imshow('1',res1)
#cv2.imshow('2',res2)
#cv2.imshow('3',res3)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
