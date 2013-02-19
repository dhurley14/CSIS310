import math #, pylab
#For newton's method, compute the two equations
# x^3 -1 = Cos(x)
# == x^3 - 1 - Cos(x) = 0 and use this equation for
# finding the root.
def fnc(x):
    y = math.cos(x)
    return y
def fncTwo(x):
    y = x*x*x - 1
    return y
def fncPrime(x):
    y = -1*math.sin(x)
    return y
def fncTwoPrime(x):
    y = (3*x*x)
    return y
def fncDas(x):
    y = (x*x*x-1-math.cos(x))
    return y
def fncDasPrime(x):
    y = (3*x*x+math.sin(x))
    return y

def newton(x,tol):
    x1 = x
    x2 = 1+x
    count = 0
    
    if (fncDas(x1) != 0 and fncDasPrime(x1) != 0):
        while (math.fabs(x2-x1)>(tol*2) or math.fabs(fncDas(x1))>(tol*2)):
            x2 = x1 - fncDas(x1)/fncDasPrime(x1)
            x1 = x2
            count = count + 1
            print count
    
    return [count,(x1+x2)/2] #return the average


z = newton(0.5,0.00001)
print ""
print z
print ""
