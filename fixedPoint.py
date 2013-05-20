import pylab

x0 = 0.3
mu = 2.0
n = 100

x=[0.0]*n
t=[0.0]*n

x[0] = x0
t[0] = 0

for i in range(n-1):
    x[i+1] = x[i]*mu*(1-x[i])
    t[i+1] = i+1

pylab.plot(t,x,'.')
pylab.show()
