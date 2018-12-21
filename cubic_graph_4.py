import math

#Define a "data class" called XYPoint.
# This class's job is not to really do any transforming or operating...
# Its job is just to REPRESENT SOME DATA. specifically it represents an xy point
class XYPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# This is not a data class because it operates on data rather than representing it.
class PowerOperator:
    def __init__(self, power):
        self.power = power
    
    def _transform(self, value):
        return math.pow(value, self.power) # calculate the root of the value and return the value

    def transform(self, value):
        if type(value) is list:
            newList = []
            for x in value:
                newList.append(self._transform(x))
            return newList
        elif type(value) is int:
            return self._transform(value)

# This is not a data class because it operates on data rather than representing it.
class MathFunction:
    def __init__(self, operator):
        self.operator = operator

    def makeXYPoints(self, xValues):
        yValues = self.operator.transform(xValues)
        i = 0
        xyPoints = []
        for xVal in xValues:
            yVal = yValues[i]
            xyPoint = XYPoint(xVal, yVal)
            xyPoints.append(xyPoint)
            i += 1
        return xyPoints

# This is could be considered a data class because it does represent a list of xypoints.
# it helps express the xypoints through the printGraph() helper function.
class MathGraph:
    def __init__(self, xyPoints):
        self.xyPoints = xyPoints

    def printGraph(self):
        for p in self.xyPoints:
            print('[' + str(p.x) + ',' + str(p.y) + '],')




############################# EXECUTION #############################

#Make a new power operator which raises numbers to the power of 3 (e.g. 2^3 = 8)
cubicPowerOperator = PowerOperator(3)

#Make a new function which can apply the operator and create a list of xyPoints
cubicPowerFunction = MathFunction(cubicPowerOperator)

#Prepare some random values to put into the function
xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Send these values to the cubicPowerFunction and get the xyPoints
xyPoints = cubicPowerFunction.makeXYPoints(xValues)

#Create a new graph object based off these points
simpleCubicPowerGraph = MathGraph(xyPoints)

#Print the graph
simpleCubicPowerGraph.printGraph()



