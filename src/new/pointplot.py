from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import position
import time
start = time.time()
fig = pyplot.figure()
ax = Axes3D(fig)
for i in range(1, 171):
    ax.scatter(position.getPosition(1, i)[0][0], position.getPosition(1, i)[0][1], [position.getPosition(1, i)[0][2]])
    print i

pyplot.show()
print time.time() - start