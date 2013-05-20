# Devin Hurley
# CSIS310 Project
# 04/19/2013

from numpy import matrix
import pylab
import math
import csv
count = 0
fields = 259
plusTwentyEight = 287
records = [0.0]*fields
with open('file.csv','r') as textfile:

    for row in reversed(list(csv.reader(textfile))):
        records[count] = row[1]
        count = count + 1        
# do it again
count = 0
moreRecordsFields = 288
moreRecords = [0.0]*moreRecordsFields
with open('somefile.csv','r') as textfile:

    for row in reversed(list(csv.reader(textfile))):
        moreRecords[count] = row[1]
        count = count + 1

        
#print len(records)
#print count
myint = 0.0
Y = [0.0]*fields
X = [0.0]*fields
for i in range(fields):
    X[i] = i
    
moreX = [0.0]*moreRecordsFields
for i in range(moreRecordsFields):
    moreX[i] = i
# RESET to 50
FREQ = 259

#polyfit algorithm
def polyfit(x,y,m):    # we want this function to output coefficients
    N=len(x)
    b = matrix([[0.0]] *(m+1)) # column vector
    M = matrix([[0.0]*(m+1)]*(m+1))
    for k in range(m+1):
        for i in range(N):
            b[k] = b[k] + float(y[i])*float(x[i])**(k)

    for k in range(m+1):
        for j in range(m+1):
        # lets begin to make the sum over i, the other part of the succinct equation
            for i in range(N):
                M[k,j] = M[k,j] + float(x[i])**float(k+j)
    a = (M.I)*b
    return a
    
# Run polyfit to test it
print polyfit(X,records,3)

# Real Fourier part
def FourierR(Array):
    # yields the real component of the Fourier Transform
    toReturn = [0.0]*fields
    for k in range(FREQ):
        for j in range(len(Array)):
            toReturn[k] = toReturn[k]+(float(Array[j]))*math.cos((2*math.pi*j*k)/fields)
            
    return toReturn

# yields the imaginary component of the Fourier Transform
def FourierI(Array):
    IReturn = [0.0]*fields
    for k in range(FREQ):
        for j in range(len(Array)):
            IReturn[k] = IReturn[k]+(float(Array[j]))*math.sin((2*math.pi*j*k)/fields)
    return IReturn

# variables to hold the outputs

# Should try to grab the coeff from the polyfit call.
# function with the polyfit coefficients
def myFunction(x):
    return 4.5799*10**(-7)*float(x)**3-1.2756*10**(-4)*float(x)**2+9.9058*10**(-3)*float(x)+3.6892*10**(-1)

#oneMoreY holds the Y points of our polyfit function
oneMoreY = [0.0]*plusTwentyEight
for i in range(plusTwentyEight):
    oneMoreY[i] = myFunction(i)

# difference is the vector of the actual data points - our polyfit datapoints
diff = [0.0]*fields
for i in range(fields):
    diff[i] = float(records[i]) - float(oneMoreY[i])


# vectors to hold the transform data
R_Points = FourierR(diff)
I_Points = FourierI(diff)

#Power Spectrum

for i in range(fields):
    Y[i] = R_Points[i]*R_Points[i] + I_Points[i]*I_Points[i]

# next we will calculate the frequency
# each point Y[k] has an associated frequency f[k] = (k-1)/tau*N
tau=1.0   #time unit (1 month)
f = [0.0]*fields
for i in range(fields/2):
    f[i] = i/(fields*tau)

#kill the zero mode
Y[0]=0
#for i in range(len(Y)):
#    Y[i] = 0

# Display graph

# next step is to find three highest frequency points tHF
# tHF = threeHighestFrequencies
tHF = [0.0,0.0,0.0,0.0]
Yone = 0.0
Ytwo = 0.0
Ythree = 0.0
Yfour = 0.0


# find the four highest frequencies in the transform.
# makes sure my FT is working
for i in range(1,len(f)-1):
    # save frequency if Y[i-1]<Y[i] and Y[i+1]<Y[i] (peaks)
    if(Y[i-1]<Y[i] and Y[i+1]<Y[i] and Y[i] > Yone):
        Yone = Y[i]
        tHF[0] = f[i]
        print tHF[0]
    elif(Y[i-1]<Y[i] and Y[i+1]<Y[i] and Y[i] > Ytwo):
        if(tHF[1]<f[i]):
            tHF[1] = f[i]
            Ytwo = Y[i]
            print tHF[1]
    elif(Y[i-1]<Y[i] and Y[i+1]<Y[i] and Y[i] > Ythree):
        if(tHF[2]<f[i]):
            Ythree = Y[i]
            tHF[2] = f[i]
            print tHF[2]
    elif(Y[i-1]<Y[i] and Y[i+1]<Y[i] and Y[i] > Yfour):
        if(tHF[3]<f[i]):
            Yfour = Y[i]
            tHF[3] = f[i]
            print tHF[3]

print tHF
print Yone,Ytwo,Ythree,Yfour

# Inverse Fourier Transform
# currently reconstructs the ORIGINAL GRAPH


### if we use Y, we compute power spectrum
### if we use the R_Points and I_Points, we get the Inverse Fourier Transform.
newY = [0.0]*fields
for i in range(fields):
    newY[i] = newY[i]/fields
    for k in range(fields):
    # R and I_Points held the data point 323 times the original
    #therefore I needed to multiply the points at that array index
    # by 1/fields, or the ratio of the number of points I have
        newY[i] = newY[i] + (float(I_Points[k])*1/fields)*math.sin((((2*math.pi*i)/1)*k)/fields)+(float(R_Points[k])*1/fields)*math.cos((((2*math.pi*i)/1)*k)/fields) # imaginary part  

print "our new function"
print polyfit(X,newY,3) # where our frequencies are at 20 points

### I WANT TO BE ABLE TO MODIFY THE POLYFIT COEFFICIENTS BASED
### OFF OF THE RESULTING MATRIX OUTPUTS FROM THE POLYFIT FNC


def newPolyFitFnc(x):
    #return 2.0981*10**(-13)*x**3+3.6036*10**(-11)*x**2+4.7875*10**(-8)*x+2.6439*10**(-6)
    return 1.1939*10**(-8)*x**3+1.8475*10**(-5)*x**2-3.3666*10**(-3)*x+9.93484*10**(-1)
newPolyValY = [0.0]*plusTwentyEight
for i in range(plusTwentyEight):
    newPolyValY[i] = newPolyFitFnc(i)

############################################################
####IFT of cleaned difference minus original difference####
############################################################

newDiff = [0.0]*fields
for i in range(fields):
    newDiff[i] = newY[i] - diff[i]
    

########## This stuff had I_Points and R_Points initially, now contain Y ###########
#newY = (1/fields)*newY

### Inverse Fourier Transform
### constructs a graph using only the first four frequencies
### from the FT.  These are found in tHF

### this loop computes the best fit line for the fourier transform we found using
### the difference between the real data points and the polynomial fit values.
dasX=[0.0]*plusTwentyEight
for i in range(plusTwentyEight):
    dasX[i] = i
dasY = [0.0]*plusTwentyEight
for i in range(plusTwentyEight): # next 28 
    dasY[i] = dasY[i]
    for k in range(FREQ): 
    # R and I_Points held the data point 323 times the original
    #therefore I needed to multiply the points at that array index
    # by 1/fields, or the ratio of the number of points I have
        dasY[i] = dasY[i] + ((float(R_Points[k])/plusTwentyEight)*math.cos(2*math.pi*k/fields*i)) + ((float(I_Points[k])/plusTwentyEight)*math.sin(2*math.pi*k/fields*i))


### finalY is the vector that holds the two best fit components.
### This will be our prediction.
finalY = [0.0]*plusTwentyEight
for i in range(fields-1,plusTwentyEight):
    finalY[i] = dasY[i] + oneMoreY[i] 
        
anX = [0.0]*plusTwentyEight
for i in range(len(anX)):
    anX[i] = i

"""
if(finalY[322]>3.0):
    print finalY[322]
    """
pylab.hold(True)

#pylab.plot(X,Y)             # Fourier Transform
pylab.plot(X,records)
pylab.plot(moreX, moreRecords)
#pylab.plot(X,newY)          #CLEANED IFT WITH 'FREQ' POINTS
#pylab.plot(dasX,dasY)
#pylab.plot(anX,oneMoreY)    # this is the function polyfit
#pylab.plot(anX,newPolyValY) # this is the IFFT diff polyfit
#pylab.plot(X,diff)  
#pylab.plot(X,newDiff)  
pylab.plot(anX,finalY)      # this is our prediction
pylab.show()

