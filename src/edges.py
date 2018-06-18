import numpy as np
import cv2
from os import listdir
from os.path import isfile,join

#The directory of the images
imagesDIR = '/Users/Steven/Desktop/Projects/SRP/TrainTracks/'
#Put image file name into list
files = [f for f in listdir(imagesDIR) if isfile(join(imagesDIR,f)) and f[len(f)-4:]=='.JPG']
#Number of current images edged and written
count = 0
#Loop through image file names
for file in files:
    #Set path to current image
    fileDIR = imagesDIR + file
    #Store current image as greyscale
    image =cv2.imread(fileDIR,0)


    '''
    This section converts the grayscaled image to an edged imaged using the Canny algorithm
    See: https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html
    Mean computes the average shade of gray in the grayscaled image.
    Ths is then used compute the correct min and max thresholds for the Canny algorithm to properly locate edges.
    See:https://stackoverflow.com/questions/24862374/canny-edge-detector-threshold-values-gives-different-result
    See: https://stackoverflow.com/questions/35586206/how-to-get-an-average-pixel-value-of-a-gray-scale-image-in-python-using-pil-nump
    '''
    mean = np.mean(image)
    edges = cv2.Canny(image,0.66 * mean,1.33 * mean)

    #The  path to save the new outline and edged images
    savepath = '/Users/Steven/Desktop/Projects/SRP/TrainTracks/outlines/'
    #Save the new image
    cv2.imwrite(join(savepath,file),edges)
    #Add one to the current count
    count += 1
    #Print the current count
    print(str(count) + " files edged and written")
print("Done!")



