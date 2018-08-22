from tkinter import *
from tkinter import filedialog
import Height
root = Tk()
root.update()

def Start():
    global root
    files = filedialog.askopenfilenames(parent=root,title='Choose a file')
    root.update()
    list_files = list(files)
    height = Height.Height(list_files)
    
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
openImages= Button(root, text="Open Images", command=lambda: Start())
openImages.pack()

root.update()
root.mainloop()
