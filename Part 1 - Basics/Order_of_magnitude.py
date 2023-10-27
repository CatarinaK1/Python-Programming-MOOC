# Please write a program which asks the user 
# for an integer number. The program should 
# then print out the magnitude of 
# the number according to the examples

# Write your solution here
number = int(input("Please type in a number: "))

if number < 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")

elif number < 100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")

elif number < 1000:
    print("This number is smaller than 1000")
    print("Thank you!")

else:
    print("Thank you!")





