# Devin Hurley
# 03/14/2013

from numpy import matrix
import pylab
from numpy import polyfit

# define 
def polyfit(x,y,m):    # we want this function to output coefficients
    N=len(x)
    b = matrix([[0.0]] *(m+1)) # column vector
    M = matrix([[0.0]*(m+1)]*(m+1))
    for k in range(m+1):
        for i in range(N):
            b[k] = b[k] + y[i]*x[i]**k

    for k in range(m+1):
        for j in range(m+1):
        # lets begin to make the sum over i, the other part of the succinct equation
            for i in range(N):
                M[k,j] = M[k,j] + x[i]**(k+j)
    a = (M.I)*b
    return a

def f(x):
    return (x**3)

# how do we test this? 

x = [0,1,2,3]
y = [0,1,8,27]
newY = [0.0]*len(y)
for i in range(4):
    step = i
    newY[i] = f(step)
pylab.hold(True)
pylab.plot(x,y,'o')
#pylab.show()
print polyfit(x,y,3)
# equation is y=x, in y=mx + b form.
# a (x,y,2) means a quadratic, works in higher dimension as well, add more points to the x and y.
print polyfit(x,y,3) # a straight line, i.e. a best fit line
pylab.plot(x,newY)
pylab.show()




