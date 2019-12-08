from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt
#import numpy as np
from numpy import *

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.set_title('Fig')
plt.xlabel('t(s)')
plt.ylabel('deviation(m)')


data2 = numpy.loadtxt('my_algrithem/s_line_90_1.dat')
x = data2[:, 8] - 0.200187
y = numpy.sqrt(multiply(data2[:, 0] - data2[:, 3], data2[:, 0] - data2[:, 3]) + multiply(data2[:, 1] - data2[:, 4], data2[:, 1] - data2[:, 4]))
plt.plot(x, y,'-')

data3 = numpy.loadtxt('dwa/s_line_90_1.dat')
x = data3[:, 8] - 2.38419e-07
y = numpy.sqrt(multiply(data3[:, 0] - data3[:, 3], data3[:, 0] - data3[:, 3]) + multiply(data3[:, 1] - data3[:, 4], data3[:, 1] - data3[:, 4]))
plt.plot(x, y,'-')

data4 = numpy.loadtxt('pure-pursuit/s_line_90_1.dat')
x = data4[:, 8] - 0.200166
y = numpy.sqrt(multiply(data4[:, 0] - data4[:, 3], data4[:, 0] - data4[:, 3]) + multiply(data4[:, 1] - data4[:, 4], data4[:, 1] - data4[:, 4]))
#y = data4[:, 6]
plt.plot(x, y, '-')



plt.legend(['my_algrithm', 'dwa', 'pure-pursuit'] , loc = 0 , ncol = 1)

#plt.annotate('Initial pose', xy = (1, 1), xytext = (0, 0), arrowprops = #dict(arrowstyle = "<-", connectionstyle = "arc3"))

plt.hold('on')
plt.grid('on')

plt.show()

