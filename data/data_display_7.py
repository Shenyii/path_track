from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.set_title('Fig')
plt.xlabel('X(m)')
plt.ylabel('Y(m)')

data = numpy.loadtxt('my_algrithem/s_line_180_1.dat')
plt.plot(data[:,3],data[:,4],'+')
#data2 = numpy.loadtxt('pure-pursuit/s_line_180_1.dat')
#plt.plot(data2[:,0],data2[:,1],'-')
data3 = numpy.loadtxt('dwa/s_line_180_1.dat')
plt.plot(data3[:,0],data3[:,1],'-')
data4 = numpy.loadtxt('my_algrithem/s_line_180_1.dat')
plt.plot(data4[:,0],data4[:,1],'-')
plt.legend(['global reference path' , 'dwa' , 'we algrithem'] , loc = 0 , ncol = 1)

plt.annotate('Initial pose', xy = (0, 0), xytext = (-0.25, 0.3), arrowprops = dict(arrowstyle = "<-", connectionstyle = "arc3"))

plt.hold('on')
plt.grid('on')

plt.show()

