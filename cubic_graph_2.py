import math

#define a function which raises a single number to a power
def transformPower(value, power):
    return math.pow(value, power)

#define a function which raises a list of numbers to a power AND returns a new list
def transformXValuesToPower(xValues, power):
    yValues = []
    for xVal in xValues:
        yValues.append(transformPower(xVal, power))
    return yValues

#define a function which raises a list of numbers to a power AND returns a new list
#the list contains the original number and the result number
def getXYPointsFromXValuesRaisedToPower(xValues, power):
    i = 0
    yValues = transformXValuesToPower(xValues, power)
    xyPoints = []
    for xVal in xValues:
        yVal = yValues[i]
        #We define a dictionary which contains 2 keys: "x", and "y"
        xyPoint = {
            "x":xVal,
            "y":yVal
        }
        xyPoints.append(xyPoint)
        i += 1
    return xyPoints

#print the x,y points
def printXYPoints(xyPoints):
    for p in xyPoints:
        print('[' + str(p["x"]) + ',' + str(p["y"]) + '],')

############################# EXECUTION #############################

#Define the x values
xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#raise the values to the power of 3 and get the values as (x,y) points
xyPoints = getXYPointsFromXValuesRaisedToPower(xValues, 3)

#print the oints
printXYPoints(xyPoints)