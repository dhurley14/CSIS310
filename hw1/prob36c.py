# Devin Hurley
# 02/17/2013
# problem 36, involving Muller's method
# CSIS310
import math

def fnc(x):
    y = math.log(2*x*x,math.exp(1))
    return y
def negFnc(x):
    y = -1*math.sqrt((math.exp(x)/2))
    return y

def fixedPointFnc(x, tol):
    x1 = x
    x2 = 1+x
    lineCount = 0
    while (math.fabs(x2-x1) > (tol*2)):
        x1 = fnc(x1)
        x2 = x1
        lineCount += 1
    if(x > 0):
        return [lineCount, (x1 + x2)/2]
    else:
        return[lineCount, -1*(x1+x2)/2]

print ""
print fixedPointFnc(2.6, 0.00001)
print ""

