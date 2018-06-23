
import sys

#must install exifread first!

from exifread.tags import DEFAULT_STOP_TAG, FIELD_TYPES
from exifread import process_file, exif_log, __version__
from os import listdir
from os.path import isfile, join

#must install re first!
import re

def sorted_nicely( l ):
    """ Sorts the given iterable in the way that is expected.
 
    Required arguments:
    l -- The iterable to be sorted.
 
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

#Specify where pictures are found
subjectdir='/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/Images/raw_images/'

onlyfiles = [f for f in listdir(subjectdir) if isfile(join(subjectdir, f)) and f[len(f)-4:]=='.JPG']

onlyfiles = sorted_nicely(onlyfiles)

#open output file and write headings -extract 'GPS' headings only
outfile=open("/Users/Steven/Desktop/Projects/SRP/MonmouthSRPImage/src/project_files/datafile.csv", 'w')
headings="FileName, GPS GPSAltitude Ratio, GPS GPSAltitudeRef Byte, GPS GPSLatitude Ratio, GPS GPSLatitudeRef ASCII, GPS GPSLongitude Ratio, GPS GPSLongitudeRef ASCII, GPS GPSVersionID Byte\n"
outfile.write(headings)

# output info for each file
for fname in onlyfiles:
    try:
        img_file = open(subjectdir+fname, 'rb')
    except IOError:
        print("unreadable", fname)
        continue
    filestuff=fname+","
    # get the tags
    data = process_file(img_file)
    if 'JPEGThumbnail' in data:
            del data['JPEGThumbnail']
        
    tag_keys = list(data.keys())
    tag_keys.sort()
    print(tag_keys)
    
    for i in tag_keys:

        #output GPS tags only
        if i[0:3]=='GPS':
            try:
                print(i)
                filestuff = filestuff+(data[i].printable).replace(',',':')+","
            except:
                print(i, str(data[i]))
    outfile.write(filestuff+'\n')

outfile.close()    
print("Files processed:", len(onlyfiles))
print("")
