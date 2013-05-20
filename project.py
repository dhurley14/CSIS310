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
    Y[i] = myint

def FourierR(Array):
    # yields the real component of the Fourier Transform
    toReturn = [0.0]*fields
    for k in range(fields):
        Array[k] = records[k]
   
    for j in range(len(Array)-1):
        toReturn[j+1] = (float(Array[j+1]))*math.cos((2*math.pi*j*j)/fields)
    return toReturn

# Display graph
newPoints = FourierR(records)
print newPoints
pylab.hold(True)
#pylab.plot(Y,records)
pylab.plot(Y,newPoints)
pylab.show()
