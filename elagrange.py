# Devin Hurley
# Homework 3, problem 3.6
# CSIS310
# 03/07/2013

import math

def eFnc(x): # multiple derivatives yield the same function.
    return math.exp(x)

def errorFnc(x,X,n):
    # n represents the degree of the polynomial
    # x represents the interpolation point we are checking
    # X represents the list of x values we are given
    prod = (x-X[0])
    for i in range(1,len(X)):
        prod = prod*(x-X[i])
    prod = prod/(math.factorial(n+1))
    prod = prod*eFnc(x)
    return prod


def lagrange(x,X,Y):
    sum = 0
    for i in range(len(X)):
        P = 1
        for j in range(len(X)):
            if j != i:
                P = P * (x-X[j])/(X[i] - X[j])
        sum = sum + P*Y[i]
    return sum


X = [0,1,2]
Y = [1,2.7183,7.3891]
print "This is the Lagrangian interpolation: " + str(lagrange(1.3,X,Y))
print ""
print "The minimum error is: " + str(errorFnc(1.3,X,2))
print ""
print "The maximum error is: " + str(errorFnc(1.3,[0,2],2))
