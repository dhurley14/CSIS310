# Devin Hurley
# 03/05/2013
# Bezier curves
# CSIS310


import math, pylab

def combinatorial(n,k):
    y = math.factorial(n)/(math.factorial(k) * math.factorial((n-k)))
    return y

def Bernstein(t,X,Y):
    n = len(X)-1
    sumx = 0
    sumy = 0
    for i in range(n+1):
        sumx = sumx + combinatorial(n,i)*((1-t)**((n)-i))*(t**i)*X[i]
        sumy = sumy + combinatorial(n,i)*((1-t)**((n)-i))*(t**i)*Y[i]
    return [sumx,sumy]


x = [0,1,15,3]
y = [0,1,2,-0.5]

a = [0.0]*101
X = [0.0]*101
Y = [0.0]*101
for k in range(101):
    a = Bernstein(k*0.01,x,y)
    X[k] = a[0]
    Y[k] = a[1]
pylab.hold(True)
pylab.plot(X,Y)
pylab.plot(x,y,'o')
pylab.show()

#    print "hello"
