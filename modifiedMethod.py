import math, pylab
from numpy import matrix


def fnc(x):
    y = math.sqrt((4-x*x)) + math.exp(x) - 1.0
    return y

def fncD(x):
    y = .5*(1/(math.sqrt(4.0-x*x))) + math.exp(x)
    return y

def newtonian(x, tol):
    x1 = x
    x2 = x + 1.0
    lineCount = 0
    while (math.fabs(fnc(x1)) > (tol*2.0)):
        print lineCount
        x2 = x1
        x1 = x1 - fnc(x)/fncD(x)
        lineCount = lineCount + 1
    return[lineCount, (x1+x2)/2]

print ""
print newtonian(0.5, 0.001)
print ""
