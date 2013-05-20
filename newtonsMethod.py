# Devin Hurley

import math, pylab
from numpy import matrix


def fnc(x,y):
    a = matrix([[x*x+y*y-4],[math.exp(x)+y-1]])
    return a

def jacobian(x,y):
    a = matrix([[2*x,2*y],[math.exp(x),1]])
    return a

#print jacobian(2,2)

def newtonian(x,y,tolerance):
    x1 = x
    y1 = y
    x2 = x +1
    y2 = y + 1
    z = [0.0]*
