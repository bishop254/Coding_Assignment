from enum import Flag
from fractions import Fraction
import math
from random import randint
from pprint import pprint



def fermatNM(n):
    # Given a fraction like 3/7, we can raise it to a number n
    # Subtract the result from 1
    # Then raise the result to 1/n
    # Finding it recipricol to obtain a second fraction 
    # The first fraction and the second when raised to n allows us to obtain the numbers (a,b,c) which almost satisfy the equation (a^n+b^n=c^n)
    
    firstFraction = None #stores the first fraction
    bFractionsArray = list() # stores possible second fractions
    numbersResult = list() # stores all the results of combinations that pass tests in the script
    
    # if n is less than 2 then exit the program
    if n <= 2:
        exit()
    
    # Generate a random integer for the numerator and denominator of the first fraction
    numerator = randint(1, 1000) 
    denominator = randint(1, 1000)
    
    # Switches the numbers if the numerator is larger than the denominator
    if numerator > denominator :
        temp = numerator
        numerator = denominator
        denominator = temp
    
    
    fractionA = Fraction(numerator, denominator) #  This is our first fraction
    firstFraction = fractionA
    
    #Perform calculations to get the second fraction
    aCalculations = math.pow(fractionA, n)
    aRemainder = 1 - aCalculations
    aRecipricol = math.pow((aRemainder), (1/n))
    
    tempArray = list() # a temporary list to store generated second fractions
    maxDenom = [10, 100] # limits to how big our fractions will become
    
    # loop through the maxDenom array while generating fractions for the second fraction
    for number in maxDenom:
        tempFraction = Fraction(aRecipricol).limit_denominator(max_denominator=number) # prints fraction form of an integer value
        
        # Ignores if the fraction generated is 1/1
        if tempFraction != Fraction(1,1):
            tempArray.append(tempFraction)
    
    bFractionsArray = set(tempArray) # removes duplicate elements and saves the new set to bFractionsArray variable
    
    # If the length of the array that stores second fractions is greater than zero then generate (a,b,c)
    if len(bFractionsArray) > 0:
        firstNumerator = int(str(firstFraction).split('/')[0]) # Numerator of the first fraction
        firstDenominator = int(str(firstFraction).split('/')[1]) # Denominator of the first fraction
        
        # Loops through each fraction in the bFractionsArray
        for fract in bFractionsArray:
            secondNumerator = int(str(fract).split('/')[0]) # Numerator of the second fraction
            secondDenominator = int(str(fract).split('/')[1]) # Denominator of the first fraction
            
            # Given the equation (a^n + b^n = c^n)
            firstNumber = firstNumerator * secondDenominator # Returns the number a
            secondNumber = secondNumerator * firstDenominator # Returns the number b
            thirdNumber = firstDenominator * secondDenominator # Returns the number c
            ##
            lhs = (math.pow(firstNumber, n) + math.pow(secondNumber, n)) # The calculations for the left hand side (a^n + b^n)
            rhs = math.pow(thirdNumber, n) # The calculations for the right hand side (c^n)
            
            diffRatio = lhs/rhs # It is the ratio of the right side to the left side
            
            # If the ratio is close to one, store that combination in a dictionary
            if (1.0 < diffRatio < 1.1):   
                data = {
                    'a': firstNumber,
                    'b': secondNumber,
                    'c': thirdNumber,
                    'diff': (lhs/rhs)
                }
                
                numbersResult.append(data) # Add this data to our combinations array stored in numbersResult
            
            # Print the numbersResult array
        if numbersResult != []:
            pprint(numbersResult)   
            print('\n')
        
def start():
    n = int(input("Enter the power... Should be above 2... \n"))
    trials = int(input("Enter the number of trials to be done... \n"))

    # Most trials evalute to an empty array thus the need to carry out the function over a number of iterations
    for i in range(trials):
        fermatNM(n)


if __name__ == "__main__":
    start()
    