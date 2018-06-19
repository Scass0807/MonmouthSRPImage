
import sys

#must install exifread first!

from exifread.tags import DEFAULT_STOP_TAG, FIELD_TYPES
from exifread import process_file, exif_log, __version__
from os import listdir
from os.path import isfile, join

#Specify where pictures are found
subjectdir='C:/Users/geckert/Downloads/CellTower/'

onlyfiles = [f for f in listdir(subjectdir) if isfile(join(subjectdir, f))]

#open output file and write headings -extract 'GPS' headings only
outfile=open("C:/Users/geckert/Downloads/datafile.csv", 'w')
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
    for i in tag_keys:

        #output GPS tags only
        if i[0:3]=='GPS':
            try:
                filestuff = filestuff+(data[i].printable).replace(',',':')+","
            except:
                print(i, str(data[i]))
    outfile.write(filestuff+'\n')

outfile.close()    
print("Files processed:", len(onlyfiles))
print("")
