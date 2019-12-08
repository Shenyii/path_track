from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.set_title('Fig')
plt.xlabel('X(m)')
plt.ylabel('Y(m)')

data = numpy.loadtxt('my_algrithem/straight_line_0_1.dat')
plt.plot(data[:,3],data[:,4],'+')
#data2 = numpy.loadtxt('pure-pursuit/straight_line_0_1.dat')
#plt.plot(data2[:,0],data2[:,1],'-')
data3 = numpy.loadtxt('dwa/l_line_ob_1.dat')
plt.plot(data3[:,0],data3[:,1],'-')
data4 = numpy.loadtxt('my_algrithem/l_line_ob_1.dat')
plt.plot(data4[:,0],data4[:,1],'-')
plt.legend(['global reference path' , 'pure-pursuit' , 'dwa' , 'my_algrithem'] , loc = 0 , ncol = 1)

cir1 = Circle(xy = (1.6, 0), radius = 0.1, alpha = 0.5)
ax1.add_patch(cir1)

plt.annotate('Initial pose', xy = (0, 0), xytext = (1, -0.05), arrowprops = dict(arrowstyle = "<-", connectionstyle = "arc3"))

plt.plot(3, 3)

plt.hold('on')
plt.grid('on')

plt.show()

