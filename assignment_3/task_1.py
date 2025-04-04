'''
Task 1: Calculate Factorial Using a Function 

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''

def factorial(number:int):

    result = 1 # (since factorial of 0 is 1).

    for i in range(1,number+1):

        result *= i   #is same as result = result*i
    
    return result

def factorial_recursion(n):

    if n < 0:
        return "Undefined(negative) input"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial_recursion(n-1)


if __name__ == '__main__':

    number = int(input("Enter a number: "))

    print(f"Factorial of {number} is", factorial(number))
    print(f"Factorial of {number} is", factorial_recursion(number))