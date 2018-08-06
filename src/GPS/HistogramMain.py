import Histogram
import shutil


count = 0
group = []
for i in range(0, Histogram.weight, 1):
    for j in range(0, Histogram.weight, 1):
        if (Histogram.histedData[i][j] > 0.9):
            count = count + 1
    if(count > 7):
        group.append(i+1)
    count = 0
print group
print len(group)
#for i in range(len(group)):
 #   shutil.copy("TrainTracks/" + Histogram.onlyfiles[group[i]-1], "useful/" + Histogram.onlyfiles[group[i]-1])

