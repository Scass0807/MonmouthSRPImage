from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random
import Height

fig = pyplot.figure()
ax = Axes3D(fig)

points = Height.GPS
print points
for i in range(0,len(points)-1):
    ax.scatter(points[i][1],points[i][2],points[i][3])


pyplot.show()
