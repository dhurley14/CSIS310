# Devin Hurley
# how to plot in 3D

import math, pylab, numpy
from mpl_toolkits.mplot3d import Axes3D


X = numpy.arange(-2,2,0.1)
Y = numpy.arange(-2,2,0.1)

xg,yg = numpy.meshgrid(X,Y)

Z = numpy.sin(xg**2+yg**2)

fig = pylab.figure() # define new window for a new plot
ax = Axes3D(fig)

ax.plot_surface(xg,yg,Z,rstride=1,cstride=1,color = 'm')
pylab.show()
