from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt
#import numpy as np
from numpy import *

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.set_title('Fig')
plt.xlabel('t(s)')
plt.ylabel('w(rad/s)')


data2 = numpy.loadtxt('my_algrithem/w_line_90_1.dat')
x = data2[:, 8] - 0.95084
#y = numpy.sqrt(multiply(data2[:, 5], data2[:, 5]) + multiply(data2[:, 6], data2[:, 6]))
y = data2[:, 7]
plt.plot(x, y,'-')

data3 = numpy.loadtxt('dwa/w_line_90_1.dat')
x = data3[:, 8] - 2.38419e-07
#y = numpy.sqrt(multiply(data3[:, 5], data3[:, 5]) + multiply(data3[:, 6], data3[:, 6]))
y = data3[:, 7]
plt.plot(x, y,'-')

data4 = numpy.loadtxt('pure-pursuit/w_line_90_1.dat')
x = data4[:, 8] - 0.200171
#y = numpy.sqrt(multiply(data4[:, 5], data4[:, 5]) + multiply(data4[:, 6], data4[:, 6]))
y = data4[:, 7]
plt.plot(x, y, '-')

plt.plot(10, 3, '.')


plt.legend(['we algrithm', 'dwa', 'pure-pursuit'] , loc = 0 , ncol = 1)

#plt.annotate('Initial pose', xy = (1, 1), xytext = (0, 0), arrowprops = #dict(arrowstyle = "<-", connectionstyle = "arc3"))

plt.hold('on')
plt.grid('on')

plt.show()

