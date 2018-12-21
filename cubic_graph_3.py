import math

#Define PowerOperator class which takes an interger argument called power upon init
# this argument is the power with which to raise other numbers to.
# -> PowerOperator's job is to raise values passed to the tranform function to the power specified during init
class PowerOperator:
    def __init__(self, power):
        self.power = power
    
    #This is the heart of the class, this _transform function is a private function to the class
    # Developers who use PowerOperator never call _transform directly...
    # in programming we put an underscore _ before a function name to 
    # tell other developers not to use this method.
    def _transform(self, value):
        return math.pow(value, self.power) # calculate the root of the value and return the value

    #This is the public transform function which users of the PowerOperator class should use
    # You can pass a list of integers [1, 2, 3] or just a single integer to this function
    # It will work out what type of object you supplied and tranform the values for you automatically
    def transform(self, value):
        if type(value) is list:
            newList = []
            for x in value:
                newList.append(self._transform(x))
            return newList
        elif type(value) is int:
            return self._transform(value)

#Define MathFunction class which takes the operator argument upon init.
# the operator must be an instance of a class which contains the function transform(value)
# -> this class's job is to:
# 1) take a series of x points, 
# 2) apply the operator to the points,
# 3) return the result as list of x,y points
class MathFunction:
    def __init__(self, operator):
        self.operator = operator

    def makeXYPoints(self, xValues):
        yValues = self.operator.transform(xValues)
        i = 0
        xyPoints = []
        for xVal in xValues:
            yVal = yValues[i]
            xyPoint = {
                "x":xVal,
                "y":yVal
            }
            xyPoints.append(xyPoint)
            i += 1
        return xyPoints

#Define class MathGraph which takes a list of points upon init.
# -> MathGraph's job is to print the xyPoints supplied to it on init
class MathGraph:
    def __init__(self, xyPoints):
        self.xyPoints = xyPoints

    def printGraph(self):
        for p in self.xyPoints:
            print('[' + str(p["x"]) + ',' + str(p["y"]) + '],')




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



