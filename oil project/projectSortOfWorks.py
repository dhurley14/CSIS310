# Devin Hurley
# CSIS310 Project
# 04/19/2013




import pylab
import math
import csv
count = 0
fields = 323
records = [0.0]*fields
with open('file.csv','r') as textfile:

    for row in reversed(list(csv.reader(textfile))):
        records[count] = row[1]
        count = count + 1        

#print records
#print count
myint = 0.0
Y = [0.0]*fields
X = [0.0]*fields
for i in range(fields):
    myint = myint+1
    X[i] = myint

def FourierR(Array):
    # yields the real component of the Fourier Transform
    toReturn = [0.0]*fields
    for k in range(fields):
        for j in range(len(Array)-1):
            toReturn[k] = toReturn[k]+(float(Array[j]))*math.cos((2*math.pi*j*k)/fields)
            
    return toReturn

# yields the imaginary component of the Fourier Transform
def FourierI(Array):
    IReturn = [0.0]*fields
    for k in range(fields):
        for j in range(len(Array)-1):
            IReturn[k] = IReturn[k]+(float(Array[j]))*math.sin((2*math.pi*j*k)/fields)
    return IReturn

# variables to hold the outputs
R_Points = FourierR(records)
I_Points = FourierI(records)

moreRPoints = [0.0]*len(R_Points)
moreIPoints = [0.0]*len(I_Points)
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


# Display graph

# next step is to find three highest frequency points tHF
# tHF = threeHighestFrequencies
tHF = [0.0,0.0,0.0]
Yone = 0.0
Ytwo = 0.0
Ythree = 0.0


# find the three highest frequencies in the transform.
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
        Ythree = Y[i]
        tHF[2] = f[i]
        print tHF[2]

print tHF
print Yone,Ytwo,Ythree

# Inverse Fourier Transform
# currently reconstructs the original graph

newY = [0.0]*fields
for i in range(fields):
    newY[i] = newY[i]*1/fields
    for k in range(fields):
    # R and I_Points held the data point 323 times the original
    #therefore I needed to multiply the points at that array index
    # by 1/fields, or the ratio of the number of points I have
        newY[i] = newY[i] + (float(I_Points[k])*1/fields)*math.sin((2*math.pi*i*k)/fields)+(float(R_Points[k])*1/fields)*math.cos((2*math.pi*i*k)/fields) # imaginary part
#newY = (1/fields)*newY


pylab.hold(True)
#pylab.plot(X,Y)
#pylab.plot(X,records)
#pylab.show()
pylab.plot(f,Y)
#pylab.plot(X,newY)
pylab.show()





