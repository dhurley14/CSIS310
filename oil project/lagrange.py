import math
import pylab


def lagrange(x,X,Y):
    Sum = 0
    for i in range(len(X)):
        P = 1
        for j in range(len(X)):
            if j != i:
                P = P * (x-X[j])/(X[i] - X[j])
        Sum = Sum + P*Y[i]
    return Sum


X = [0.0,1.0,2.0,3.0]
Y = [1.0,2.0,4.0,8.0]
print ""
print (lagrange(4.0,X,Y))
print ""

step = 1.0
x = [0.0]*5
y = [0.0]*5
for i in range(5):
    x[i] = i*step
    y[i] = lagrange(x[i],X,Y)

pylab.plot(x,y)
pylab.show()


# can pylab plot three D stuff?
#pylab.plot(1,3,4)
#pylab.show()
