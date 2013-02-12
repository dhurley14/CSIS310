#SECANT METHOD
#02/07/2013
import math, pylab

def fnc(x):
    y = 3*x + math.sin(x) - math.exp(x)
    return y

def sec(a,b,tol):

    count = 0
    if fnc(b)<fnc(a):
        #swap numbers
        temp = b
        b = a
        a = temp
    c = b      #to start the loop
    while abs(fnc(c)) > tol:
        count = count + 1
        c = a-((b-a)*fnc(a))/(fnc(b) - fnc(a))
        b = a
        a = c
    return[count, c]

z = sec(0.0, 2.0, 0.000001)
print ""
print z
print ""
