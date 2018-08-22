from matplotlib import pyplot

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import platform
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


highlight = ax.scatter([], [],[],color='blue')


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
        file = selectedImageName
        if platform.system() == 'Windows':
            os.system("taskkill /f /im Microsoft.Photos.exe /t")
            os.system('"' + file + '"')
        elif platform.system() == 'Darwin':
            os.system("osascript -e 'quit app \"Preview\"'")
            os.system("open " + file)

    pyplot.draw()
fig.canvas.mpl_connect('pick_event', onpick)
pyplot.show()

