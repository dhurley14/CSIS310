# Devin Hurley
# 03/21/2013
# classic integration approximation
# using trapezoidal method

import math

def fnc(x):
    return math.exp(-x**2)
    
#integrate e^-(x^2)
def trap(a,b,n):
    # Compute integral from a to b given n points.
    delta = abs(a-b)/n
    I = 0.0
    for k in range(1,n):
        x = a + delta*k
        I = I + fnc(x)*2.0    
    I = (I+fnc(a)+fnc(b))*delta/2.0
    return I

for n in range(1.0,100.0):
    
    print trap(0.0,1.0,n)
