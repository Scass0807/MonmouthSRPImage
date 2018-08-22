import sys
from exifread.tags import DEFAULT_STOP_TAG, FIELD_TYPES
from exifread import process_file, exif_log, __version__
from os import listdir
from os.path import isfile, join
import numpy as np
import re
class Height:
    def __init__(self,files):
        onlyfiles = files
        # output info for each file
        onlyfiles = self.sorted_nicely(onlyfiles)
        height = []
        latitude = []
        longitude = []
        for fname in onlyfiles:
            try:
                img_file = open(fname, 'rb')
            except IOError:
                print("unreadable", fname)
                continue
            # get the tags
            data = process_file(img_file)
            if 'GPS GPSAltitude' in data:
                ref = int(data['GPS GPSAltitudeRef'].printable)
                if ref==1:
                    height.append(-1 *(self.divided(data['GPS GPSAltitude'].printable)))
                else:              
                    height.append(self.divided(data['GPS GPSAltitude'].printable))
            if 'GPS GPSLatitude' in data:
                latitude.append(self.analyze(data['GPS GPSLatitude'].printable))
            if 'GPS GPSLongitude' in data:
                longitude.append(self.analyze(data['GPS GPSLongitude'].printable))

        flag = []
        for fname in onlyfiles:
            flag.append(fname)
        self.GPS = [[flag[i]] + [latitude[i]]+ [longitude[i]] + [height[i]] for i in range(len(onlyfiles))]
        print(self.GPS)
        
    def sorted_nicely(self,name):
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(name, key=alphanum_key)

    def divided(self,a):
        position = a.find('/')
        numerator = a[:position]
        denominator = a[position+1:]
        return float(int(numerator)/float(denominator))

    def analyze(self,a):
        position = a.find(',')
        a = a [position+1:]
        position = a.find(',')
        a = a[position+2:len(a)-1]
        return self.divided(a)

#print  name
#name.sort(key=lambda x : x[1])
#print name

##
