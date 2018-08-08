from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random
import Height

fig = pyplot.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = list(range(0, 100))
sequence_containing_y_vals = list(range(0, 100))
sequence_containing_z_vals = list(range(0, 100))

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)
points = Height.GPS

for i in range(0,len(points)-1):
    ax.scatter(points[i][1],points[i][2],points[i][3])
    print (i)

pyplot.show()
