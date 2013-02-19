# Devin Hurley
# CSIS310
# 02/17/2013
# part a - derivative of f is 
#
# 12*x^2 - x*e^((x^2)/2)
#
# part b - at x = 2
# it reaches the root near 1
# 
# problem number 13

import math

def fnc(x):
    y = 4*(x*x*x) -1 - math.exp((x*x)/2)
    return y
def fncPrime(x):
    y = 12*x*x - x*math.exp((x*x)/2)
    return y

def newtonian(x, tol):
    x1 = x
    x2 = 1+x
    lineCount = 0
    while(math.fabs(x2-x1) > (tol*2) or math.fabs(fnc(x1)) > (tol*2)):
        x2 = x1 - fnc(x1)/fncPrime(x1)
        x1 = x2
        lineCount = lineCount + 1
    return [lineCount, (x1 + x2)/2]


print ""
z = newtonian(3.0, 0.0001)
print z
print ""
