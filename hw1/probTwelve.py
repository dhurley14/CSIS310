import math #, pylab

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
    y = (3*x*x)-1
    return y

def newton(x,tol):
    x1 = x
    x2 = 1000000
    count = 0
    
    if (fnc(x1) != fncTwo(x1) and fncPrime(x1) != fncTwoPrime(x1)):
        while (math.fabs(x2-x1)>(tol*2) or math.fabs(fnc(x1))>(tol*2)): # or  math.fabs(fncPrime(x1)) != math.fabs(fncTwoPrime(x1))):
            x2 = x1 - fnc(x1)/fncPrime(x1)
            x1 = x2
            count = count + 1
            print count
    
    return [count,x1] #return the average


z = newton(0.5,0.00001)
print ""
print z
print ""
