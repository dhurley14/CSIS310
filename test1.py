#Devin Hurley
#01/30/2013
#CSIS 310

import math, pylab



Npoints = 200

# spacing between the points

delta = 0.1

angle = [0.0]*Npoints
y = [0.0]*Npoints

for i in range(Npoints):
    angle[i] = delta*i
    y[i] = math.cos(angle[i])
    #print angle, math.cos(angle)
   
pylab.plot(angle,y)
pylab.show()
