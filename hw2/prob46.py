# Devin Hurley
# Numerical Methods HW problem 46
# 02/22/2013
# Using x = g(x) method.

import math


def fnc(x):
    y = (x*x) + (math.cos(x)**2)**2 - 2.0
    return y

def fixedPoint(x, tol):
    x1 = x
    x2 = 1 + x
    while(math.fabs(x2 - x1)>(tol*2)):
        x1 = fnc(x1)
        x2 = x1
    return (x1+x2)/2

print""
print fixedPoint(-1.0,.0000000001)
print""


