# Please write a program which asks the user to type in an integer number. 
# If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.

# The factorial of a number involves multiplying the number by all the positive integers smaller than itself. 
# In other words, it is the product of all positive integers less than or equal to the number. 
# For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.






while True:
    factorial = 1
    Result = 1
    
    number = int(input("Please type in a number: "))
    
    if number < 1:
        break


    while factorial <= number:
        Result *= factorial
        factorial += 1

    print(f"The factorial of the number {number} is {Result}")


print("Thanks and bye!")