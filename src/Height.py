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
    return int(int(numerator)/int(denominator))

# get the picture
subjectdir = 'C:/Users/nianq/Desktop/image recog/celltower/'
onlyfiles = [f for f in listdir(subjectdir) if isfile(join(subjectdir, f))]
# output info for each file
onlyfiles = sorted_nicely(onlyfiles)
height = []
for fname in onlyfiles:
    try:
        img_file = open(subjectdir + fname, 'rb')

    except IOError:
        print("unreadable", fname)
        continue
    # get the tags
    data = process_file(img_file)

    if 'GPS GPSAltitude' in data:
        height.append(divided(data['GPS GPSAltitude'].printable))

flag = [i for i in range(1,len(onlyfiles)+1)]
name = [[flag[i]] + [height[i]] for i in range(len(onlyfiles))]
print name
#print  name
#name.sort(key=lambda x : x[1])
#print name
##