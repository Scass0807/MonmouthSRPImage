from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random


fig = pyplot.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = list(range(0, 100))
sequence_containing_y_vals = list(range(0, 100))
sequence_containing_z_vals = list(range(0, 100))

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

ax.scatter(0.0358, -0.133, 0.089)
ax.scatter(-0.48, -0.0117, 0.31)
ax.scatter(0,0,0)
pyplot.axis([-1, 1, -1, 1])

pyplot.show()
