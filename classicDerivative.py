import math

def fnc(z):
    return z/3.0

def deriv(x):
    toReturn = 0.0
    for i in range(1,10):
        h = 1.0/(2.0**i)
        num = fnc(x+h) - fnc(x)
        toReturn = num/h
    return toReturn




print deriv(2.0)
