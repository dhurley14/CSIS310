#SECANT METHOD
#02/07/2013
import math #, pylab

def fnc(x):
    y = 2*math.sin(x) - math.exp(x)/4 - 1
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

z = sec(-5.0, -3.0, 0.00001)
k = sec(-7.0, -5.0, 0.00001)
print ""
print z
print ""
print k
print ""
