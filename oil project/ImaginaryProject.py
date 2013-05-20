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
   
    for j in range(len(Array)-1):
        toReturn[j] = (float(Array[j]))*math.cos((2*math.pi*j*j)/fields)
    return toReturn
def FourierI(Array):
    # yields the imaginary component of the Fourier Transform
    IReturn = [0.0]*fields
    for j in range(len(Array)-1):
        IReturn[j] = (float(Array[j]))*math.sin((2*math.pi*j*j)/fields)
    return IReturn




# Display graph
R_Points = FourierR(records)
I_Points = FourierI(records)


for i in range(fields):
    Y[i] = R_Points[i]*R_Points[i] + I_Points[i]*I_Points[i]
print records
#print f
#print newPoints
pylab.hold(True)
#pylab.plot(X,Y)
pylab.plot(X,records)
#pylab.show()

pylab.show()




