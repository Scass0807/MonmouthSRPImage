from matplotlib import pyplot

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import Height
import subprocess
fig = pyplot.figure()
ax = Axes3D(fig)
imagePath = Height.subjectdir
points = Height.GPS
print (points)
for i in range(0,len(points)):
    ax.scatter(points[i][1],points[i][2],points[i][3], color='orange',picker=1)


def FindImage(x,y,z):
    for i in range(len(points)):
        if(x==points[i][1] and y == points[i][2] and z == points[i][3]):
            return points[i][0]
    return 'Not found'

<<<<<<< HEAD
ax2 = pyplot.subplot2grid((4,10),(0,6),rowspan =4,colspan=4)
highlight = ax.scatter([], [],[],color='blue')               
=======
highlight = ax.scatter([], [],[],color='blue')


>>>>>>> 80a9b1a63186d41af5273783794867de6210b530
def onpick(event):
    global imagePath
    global highlight

    highlight.remove()
    ind = event.ind[0]
    x, y, z = event.artist._offsets3d
    print((x[ind],y[ind],z[ind]))
    highlight = ax.scatter(x[ind], y[ind], z[ind], color='blue')
    selectedImageName = FindImage(x[ind],y[ind],z[ind])

    if selectedImageName != 'Not found':
        selectedImageName = imagePath + selectedImageName
        print(selectedImageName)
        os.system("taskkill /f /im Microsoft.Photos.exe /t")
        file = selectedImageName
        os.system('"' + file + '"')

    pyplot.draw()
fig.canvas.mpl_connect('pick_event', onpick)
pyplot.show()
