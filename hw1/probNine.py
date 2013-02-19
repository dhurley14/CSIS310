#regula falsi method.
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
        c = a - fnc(a) * (b-a)/(fnc(b) - fnc(a))
        if fnc(c)<0 and fnc(b)<0 or fnc(c)>0 and fnc(b)>0:
            b=c
        else:
            a=c
    return[count, c]


z = sec(-5.0, -3.0, 0.00001)
print ""
print z
print ""
