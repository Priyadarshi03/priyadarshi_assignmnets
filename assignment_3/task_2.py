'''
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
    - Square root of the number
    - Natural logarithm (log base e) of the number
    - Sine of the number (in radians)
3.   Displays the calculated results.
'''
import math
number = float(input("Enter a number: "))

print("Square root:", math.sqrt(number))
print("Logarithm:", math.log(number))
print("Sine:", math.sin(number))