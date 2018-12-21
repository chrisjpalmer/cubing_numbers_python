import math

#Get some x values
xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#for each x value we just raise it to the power of 3...
#we print the points we get.
for xVal in xValues:
    yVal = math.pow(xVal, 3)
    print('[' + str(xVal) + ',' + str(yVal) + '],')