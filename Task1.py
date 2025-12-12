"""Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

print("Entered first number is:",num1)
print("Entered second number is:",num2)

Addition=num1+num2
Subtraction=num1-num2
Multi=num1*num2
Division=num1/num2

print("Addition:",Addition)
print("Subtraction:",Subtraction)
print("Multiplication:",Multi)
print("Division:",Division)
