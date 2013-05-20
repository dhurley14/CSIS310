import math
import pylab


def lagrange(x,X,Y):
    sum = 0
    for i in range(len(X)):
        P = 1
        for j in range(len(X)):
            if j != i:
                P = P * (x-X[j])/(X[i] - X[j])
        sum = sum + P*Y[i]
    return sum


X = [2.1,4.1,7.1]
Y = [-12.4,7.3,10.1]
print ""
print lagrange(8.0,X,Y)
print ""
X=[3,8]
Y=[-1.79,4.99]
step = 0.01
x = [0.0]*100
y = [0.0]*100
for i in range(100):
    x[i] = i*step
    y[i] = lagrange(x[i],X,Y)

pylab.hold(True)
pylab.plot(x,y)
pylab.plot(X,Y)
pylab.show()


# can pylab plot three D stuff?
#pylab.plot(1,3,4)
#pylab.show()
