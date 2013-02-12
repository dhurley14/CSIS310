import math, pylab

def fnc(x):
    y = 3*x + math.sin(x) - math.exp(x)
    return y

def bisec(a,b,tol):

    count = 0
    while (b-a) > (tol*2):
        c = (a+b)/2
        count = count + 1
        if fnc(a) * fnc(c) < 0:
            b=c
        else:
            a = c
    return [count,(b+a)/2] #return the average


z = bisec(0.0, 2.0, 0.000001)
print ""
print z
print ""
