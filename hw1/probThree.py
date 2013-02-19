import math #, pylab

def fnc(x):
    y = math.cos(x)
    return y
def fncTwo(x):
    y = x*x*x - 1
    return y

def bisec(a,b,tol):

    count = 0
    while (b-a) > (tol*2):
        c = (a+b)/2
        count = count + 1
        if fnc(a) != fncTwo(c) and fnc(a) < fncTwo(c):
            b=c
        elif fnc(a) != fncTwo(c) and fncTwo(c) < fnc(a):
            a = c
    return [count,(b+a)/2] #return the average


z = bisec(0.0,2.0, 0.00001)
print ""
print z
print ""
