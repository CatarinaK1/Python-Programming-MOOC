# Please write a program which asks the user for 
# two numbers and an operation. If the operation is 
# add, multiply or subtract, the program should calculate and 
# print out the result of the operation 
# with the given numbers. 
# If the user types in anything else, the program 
# should print out nothing.

# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}")

if operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")

if operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")










