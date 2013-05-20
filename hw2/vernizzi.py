#import all libraries
import math #, pylab
from numpy import matrix, linalg

#solve the system x^2+y^2=4, exp(x)+y=1
#by using the Newton method

#define the function F (from the system of equations)
def Fun(x,y):
    f1=x**2+y**2-4
    f2=math.exp(x)+y-1
    s=matrix([[f1],[f2]])
    return s

#define the derivatives of F (Jacobian)
def Jac(x,y):
    J=matrix([[2*x, 2*y],[math.exp(x),1]])
    return J

#prepare for Newton Method
def Newton(x0,y0,tol):
    x=x0;
    y=y0;
    F0=Fun(x,y)
    while(linalg.norm(F0)>tol):
        J=Jac(x,y)
        F=Fun(x,y)
        delta=-(J.I)*F
        x=x+delta[0,0]
        y=y+delta[1,0]
        F0=Fun(x,y)
    return [x,y]


#example
a=Newton(-2,2,1e-8)
print a

a=Newton(1,-3,1e-8)
print a

#'let's plot the solution

#allocate the memory
x=[0.0]*100
y1=[0.0]*100
y2=[0.0]*100
y3=[0.0]*100
dx=.04

for i in range(100):
    x[i]=-2.0+i*dx
    y1[i]=math.sqrt(4-(x[i]**2))
    y2[i]=-math.sqrt(4-x[i]**2)
    y3[i]=1-math.exp(x[i])


pylab.plot(x,y1)
pylab.plot(x,y2)
pylab.plot(x,y3)
pylab.show()
