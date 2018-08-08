
import sys
from exifread.tags import DEFAULT_STOP_TAG, FIELD_TYPES
from exifread import process_file, exif_log, __version__
from os import listdir
from os.path import isfile, join
import numpy as np
import re
def sorted_nicely(name):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(name, key=alphanum_key)

def divided(a):
    position = a.find('/')
    numerator = a[:position]
    denominator = a[position+1:]
    if(a.isdigit()):
        denominator = 0.1
    return float(float(numerator)/float(denominator))
# get the picture
subjectdir = 'C:/Users/Monmouth 001/Documents/GitHub/MonmouthSRPImage/Images/raw_images/'
onlyfiles = [f for f in listdir(subjectdir) if isfile(join(subjectdir, f))]
# output info for each file

cameraMatrix = []
fname = onlyfiles[0]
try:
    img_file = open(subjectdir + fname, 'rb')
except IOError:
    print("unreadable", fname)

# get the tags
data = process_file(img_file)
length = divided(data['EXIF ExifImageLength'].printable)
width = divided(data['EXIF ExifImageWidth'].printable)
focalLength = divided(data['EXIF FocalLength'].printable)


cameraMatrix.append([focalLength,0.0,length/2])
cameraMatrix.append([0.0, focalLength,  width / 2])
cameraMatrix.append([0.0,0.0,1.0])




#Camera matrix
#[[facol lenth, 0 , center point of length],
#[0, facol lenth, cnter point of height],
#[0,0,1 ] ]
