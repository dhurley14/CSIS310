# Devin Hurley
# 04/18/2013
from pylab import plot, show, axis, ginput # graphical input


n = 3
print "Hello... Please click here",n," times."

# create a system of axis
# use graphical input to memorize the points

axis([-1,1,-1,1])

points = ginput(n) #it will wait n clicks
print "The points selected are"

x = map( lambda x: x[0],points)
y = map(lambda x: x[1],points)

plot(x,y,'o-')

print points
show()
