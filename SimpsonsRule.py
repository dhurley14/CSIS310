# Devin Hurley
# 03/21/2013
# Simpsons rule for integration.
# Simposons 1/3 rule and Simpsons 3/8 rule
# basically an improvement over trapezoid rule.
import math

def fnc(x):
    return x/2

def trap(a,b,n):
    # Compute integral from a to b given n points.
    delta = abs(a-b)/n
    I = 0.0
    for k in range(1,n):
        x = a + delta*k
        I = I + fnc(x)*
