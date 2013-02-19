# Devin Hurley
# 02/17/2013
# problem 36, involving the fixed-point method.
# CSIS310

# part b.
# at x = 2.5, it converges to 2.4680
# at x = 2.7 it converges to 2.7276 
import math

def fnc(x):
    y = math.sqrt((math.exp(x)/2))
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
print fixedPointFnc(2.7, 0.000000001)
print ""

