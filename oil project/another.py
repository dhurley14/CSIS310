# Devin Hurley
# CSIS310 Project
# 04/06/2013

from numpy import matrix
import pylab
import math
import csv
count = 0
fields = 322
records = [0.0]*fields
with open('COMMODITY_HEATINGOIL.csv','r') as textfile:

    for row in reversed(list(csv.reader(textfile))):
        records[count] = row[1]
        count = count + 1        

#print records
#print count
myint = 0.0
Y = [0.0]*fields
X = [0.0]*fields
for i in range(fields):
    X[i] = i

# RESET to 50
FREQ = 322


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


# vectors to hold the transform data
R_Points = FourierR(records)
I_Points = FourierI(records)

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


pylab.hold(True)

pylab.plot(X,Y)
pylab.show()
