from matplotlib import pyplot

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import platform
import subprocess
class pointplot:
    def __init__(self,files,coords):
         
        self.ax = Axes3D(fig)
        self.imagePath = self.findPath(files[0])
        self.points = coords
        print (points)
        self.fig = pyplot.figure()

        for i in range(0,len(points)):
            ax.scatter(points[i][1],points[i][2],points[i][3], color='orange',picker=1)

        self.highlight = ax.scatter([], [],[],color='blue')
        pyplot.draw()
        fig.canvas.mpl_connect('pick_event', self.onpick)
        pyplot.show()
        
    def findPath(self,file):
        for n in range(len(file) - 1, -1, -1):
            if file[n] == '/' or file[n] == '\\':
                return file[0:n+1]
                 


    def FindImage(self,x,y,z):
        for i in range(len(self.points)):
            if(x==self.points[i][1] and y == self.points[i][2] and z == self.points[i][3]):
                return points[i][0]
        return 'Not found'





    def onpick(self,event):
        self.highlight.remove()
        ind = event.ind[0]
        x, y, z = event.artist._offsets3d
        print((x[ind],y[ind],z[ind]))
        self.highlight = ax.scatter(x[ind], y[ind], z[ind], color='blue')
        selectedImageName = self.FindImage(x[ind],y[ind],z[ind])

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



