# Devin Hurley
# 
import math, pylab

mu = 4.0
N = 100.0
delX = 1/N

x = [0.0]*100
y = [0.0]*100

# compute the function on these points

for i in range(100):
    x[i] = i*delX
    y[i] = mu*(mu*x[i]*(1.0-x[i]))*(1.0-(mu*x[i]*(1.0-x[i])))

pylab.plot(x,y)
pylab.show()
