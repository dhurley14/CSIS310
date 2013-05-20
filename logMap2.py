# Devin Hurley
# 
import math, pylab, random

def fnc(x,mu):
    y = mu*x*(1-x)
    return y
random.seed()
N = 500.0
mu = [0.0]*500*20
ex = [0.0]*500*20
delMu = 0.01  ## move very slowly
for i in range(500):
    m = i*delMu
    for j in range(20):
        x = random.random()
        for k in range(300):
            x = fnc(x,m)
        mu[20*i + j] = m
        ex[20*i + j] = x

"""
mu = 4.0
N = 100.0
delX = 1/N

x = [0.0]*100
y = [0.0]*100

# compute the function on these points

for i in range(100):
    x[i] = i*delX
    y[i] = mu*(mu*x[i]*(1.0-x[i]))*(1.0-(mu*x[i]*(1.0-x[i])))
"""
pylab.plot(mu,ex,'.')
pylab.show()
