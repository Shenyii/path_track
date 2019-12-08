from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.set_title('Fig')
plt.xlabel('X(m)')
plt.ylabel('Y(m)')

data = numpy.loadtxt('w_line_90_1.dat')
plt.plot(data[:,3],data[:,4],'+')
data2 = numpy.loadtxt('w_line_90_1.dat')
plt.plot(data2[:,0],data2[:,1],'-')
plt.legend(['global reference path' , 'real trajectory'] , loc = 0 , ncol = 1)
#data = numpy.loadtxt('straight_line_0_1.dat')
#plt.plot(data[:,3],data[:,4],'+')
#data2 = numpy.loadtxt('straight_line_0_1.dat')
#plt.plot(data2[:,0],data2[:,1],'-')
#plt.legend(['global reference path' , 'real trajectory' , 'global reference path2' , 'real trajectory2'] , loc = 0 , ncol = 1)

plt.hold('on')
plt.grid('on')

plt.show()

