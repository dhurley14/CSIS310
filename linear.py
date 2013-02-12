import math, pylab

def fnc(x):
    y = 3*x + math.sin(x) - math.exp(x)
    return y
Npoints = 100

xmin = -2.
xmax = 2.
step = (xmax-xmin)/Npoints
x= [0.0]*Npoints
y=[0.0]*Npoints

for i in range(Npoints):
    x[i] = xmin+i*step
    y[i]=fnc(x[i])

pylab.plot(x,y)
pylab.show()


