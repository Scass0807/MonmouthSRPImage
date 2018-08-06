import Height
import Histogram
import time

import shutil
def getHeight():

    return Height.name

start = time.time()
height = getHeight()
print height


PT = True

flag = [i for i in range(1,len(Histogram.onlyfiles)-1)]
for i in range(0, Histogram.weight-2, 1):
    group = []
    position = height[i][1]
    if (flag[i] != -1):
        for j in range(0, Histogram.weight-2, 1):

            # print "for picture " + str(i) + "and" + str(j) + str

            if (Histogram.histedData[i][j] > 0.7 and flag[j] != -1 and abs(height[j][1] - position) <= 2 ):
                flag[j] = -1
                group.append(j+1)
        print group
        if (i == 1):
            for i in range(len(group)):
                shutil.copy("TrainTracks/" + Histogram.onlyfiles[group[i] - 1],
                            "useful/" + Histogram.onlyfiles[group[i] - 1])

            PT = False



print str(time.time()-start)
