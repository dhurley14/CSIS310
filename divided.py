# Devin Hurley
# 02/28/2013
# NUMMETH
# An algorithm for Interpolation from a Divided Difference Table

# given a set of n + 1 points, [(xi, fi), i = 0,...,n] and a value x = u at which the interpolating polynomial is to be evalutated:


import math

# 1 find the coefficients of the interpolating polynomial
# these are stored in vector dd

def DDT(y,x,u):
    dd = [0.0]*len(x)
    for i in range(len(x)):
       dd[i] = y[i]
    print dd[2]
    for j in range(1,len(x)):
        temp1 = dd[j-1]
        for k in xrange(j,len(x)):
            temp2 = dd[k]
#           print "x[k]" +" "+ str(x[k])
#           print "x[k-j]" + " " + str(x[k-j])
            dd[k] = (dd[k] - temp1)/(x[k] - x[k-j])
            temp1 = temp2
    # now we compute the value of the polynomial
    # at u.  We do this by nested multiplication
    # from the highest term.
    sum = 0
    for i in range(len(x)-1,0,-1):
        sum = (sum+dd[i])*(u - x[i-1])
        sum = sum + dd[0]
    return sum
print ""
print DDT([4,5,6],[1,2,3],1)
print ""
