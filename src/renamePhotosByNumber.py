from os import listdir,rename
from os.path import isfile,join
import re

def sorted_nicely( l ):
    """ Sorts the given iterable in the way that is expected.
 
    Required arguments:
    l -- The iterable to be sorted.
 
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

#The directory of the images
imagesDIR = '/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/'
outlinesDIR ='/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/outlines/'
#Put image file name into list
files = [f for f in listdir(imagesDIR) if isfile(join(imagesDIR,f)) and f[len(f)-4:]=='.JPG']
files = sorted_nicely(files)
#Number of current images edged and written
#Loop through image file names

for number in range(len(files)):
    #Set path to current image
    imageDIR = imagesDIR + files[number]
    outlineDIR = outlinesDIR + files[number]
    rename(imageDIR,imagesDIR +str(number + 1) +'.JPG')
    rename(outlineDIR,outlinesDIR +str(number + 1) +'.JPG')
    print("Renaming " + files[number] + ' to '+ str(number + 1) +'.JPG')
    

