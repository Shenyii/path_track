from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.set_title('Fig')
plt.xlabel('X(m)')
plt.ylabel('Y(m)')

#data = numpy.loadtxt('my_algrithem/straight_line_0_1.dat')
#plt.plot(data[:, 8],data[:,5],'+')
data2 = numpy.loadtxt('pure-pursuit/straight_line_0_1.dat')
#y = data[:, 5] / numpy.cos(data[:, 2])
#x = data[:, 8]
plt.plot(data2[:,8],data2[:,5],'-')
data3 = numpy.loadtxt('dwa/straight_line_0_1.dat')
plt.plot(data3[:,8],data3[:,5],'-')
data4 = numpy.loadtxt('my_algrithem/straight_line_0_1.dat')
plt.plot(data4[:,8] - 0.800719, data4[:,5], '-')
plt.legend(['pure-pursuit' , 'dwa' , 'my_algrithem'] , loc = 0 , ncol = 1)

#plt.annotate('Initial pose', xy = (1, 1), xytext = (0, 0), arrowprops = #dict(arrowstyle = "<-", connectionstyle = "arc3"))

plt.hold('on')
plt.grid('on')

plt.show()

