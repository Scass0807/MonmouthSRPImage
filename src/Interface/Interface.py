from tkinter import *
from tkinter import filedialog
from Height import Height
import numpy as np
from matplotlib import pyplot

from mpl_toolkits.mplot3d import Axes3D
import os
import platform
import subprocess

root = Tk()
root.update()

global list_files
global GPS


def findPath(file):
    for n in range(len(file) - 1, -1, -1):
        if file[n] == '/' or file[n] == '\\':
            return file[0:n+1]
                 


def FindImage(x,y,z):
    for i in range(len(points)):
        if(x==points[i][1] and y == points[i][2] and z == points[i][3]):
            return points[i][0]
    return 'Not found'
def onpick(event):
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


def createGraph(files,coords):
        ax = Axes3D(fig)
        imagePath = findPath(files[0])
        points = coords
        print (points)
        fig = pyplot.figure()

        for i in range(0,len(points)):
            ax.scatter(points[i][1],points[i][2],points[i][3], color='orange',picker=1)

        highlight = ax.scatter([], [],[],color='blue')
        pyplot.draw()
        fig.canvas.mpl_connect('pick_event', onpick)
        pyplot.show()

def Start():
    global root
    files = filedialog.askopenfilenames(parent=root,title='Choose a file')
    root.update()
    list_files = list(files)
    height = Height(list_files)
    GPS = height.GPS
    createGraph(list_files,GPS)

welcome= Text(root, height=10, width=50)

welcome.tag_configure('title', font=('Arial', 20, 'bold'))
welcome.tag_configure('instructions', font=('Arial', 12))
welcome.tag_bind('follow', '<1>', lambda e, t=welcome: t.insert(END, ""))
welcome.insert(END,'\nWelcome\n', 'title')
message ="""
Welcome to the 3D Aerial Scatterplot Generator.
Press "Open Images" to open the images and
generate a scatter plot.
"""
welcome.insert(END,message, 'instructions')
welcome.pack(side = TOP)
openImages= Button(root, text="Open Images", command= lambda:Start())
openImages.pack()

root.update()

    
