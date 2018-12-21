## Simple Program 4 Times

Here are 4 versions of a program which takes some numbers, raises them to the power of 3, then prints the numbers as a set of x,y points - where y is x^3.

I want to emphasize that no version of code is better than the other. They are just better at different things.

## Version 1
Version 1 of the code is great because its very simple, easy to understand and gets the job done. Version 1 is very valid.

## Version 2
Version 2 of the code is great because it breaks up some of the different processes into different functions. Maybe if we need to raise some numbers to a power again, we can reuse the functions we just built. 

### DRY
This concept in programming is called DRY code (Dont repeat yourself). The basic idea is to try as hard as possible not repeat the same code over and over again in the application. We do this by putting common code into functions and calling the function instead of writing the code again.

### Tightly Bound
Version 2 is an example of 'tightly bound' code. Tightly bound code means that changing one part of the code affects another part of the code very easily. If I wanted to change the program to multiply numbers I would need to create the `transformMultiply` function, then change the `transformXValuesToPower` function to use it. I should also rename `transformXValuesToPower` -> `transformXValuesToMultiply` and `getXYPointsFromXValuesRaisedToPower` -> `getXYPointsFromXValuesRaisedToMultiply` for consistency.

If you want you think you are going to change the code a lot in the future, it is best to avoid tightly bound code and to generalize it so the code can be interchanged or swapped out easily.

## Version 3
Version 3 of the code is great because it is an example of 'loosely coupled' code. 'Loosely coupled', is the opposite of 'tightly bound'. If I want to change the application to do multiplication, I can write another class called `MultiplyOperator` and pass this to the `MathFunction` class initializer. I don't have to go renaming lots of functions in my program.

### Loosley Coupled
Version 3 is for a development team of around 10 people. The boss says to one of the programmers, "go and make a new operator which does division!". The programmer only has to create one new thing: The `DivideOperator` class. Now the boss says to another programmer, "use the `DivideOperator` class in a cool new feature of the application!" The developer just needs to pass the `DivideOperator` class to the `MathFunction` class. He doesn't need to make a new `transformXValuesToDivide` and a new `getXYPointsFromXValuesRaisedToDivide` ... which sounds pretty complicated anyway. The harder you make programming tasks, the more likely you are going to introduce bugs.

## Version 4
Version 4 is a slight variation of Version 3 and adds in the `XYPoint` class. Here all I am trying to do is show how we can use classes to operate on data (like the `MathFunction` or `PowerOperator` classes) OR represent data (`XYPoint` class).

Its not entirely necessary to do version 4 - more a matter of style. Up to you. As long as in your brain you have a clear way of knowing what is data and what is "operating on data" then you are fine!

## Summary
Each version shows you how you can represent the same idea for different purposes. If your don't have a large team maybe version 2 is good for you. If you have a large team maybe version 3 or 4 is better. If you are working on a large program by yourself... maybe start by writing version 2 and evolve it to version 3 later to make your life easier in the future. If you need to go to the toilet in a hurry, maybe just write version 1 because version 3 is overkill. Your choice!

Enjoy:)


