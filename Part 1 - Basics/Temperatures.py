# Please write a program which asks the user for 
# a temperature in degrees Fahrenheit, and 
# then prints out the same in degrees Celsius. 
# If the converted temperature falls below zero degrees Celsius, 
# the program should also print out 
# "Brr! It's cold in here!".


# Write your solution here
fahrenheit = int(input("Please type in a temperature (F): "))

celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")
