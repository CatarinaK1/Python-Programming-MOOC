# Write a Program that asks the user how old they are. 
#Then the program should ask the user if they want to know how old they are in months, days, hours or seconds.

age = int(input("What is your age?"))

months = age * 12
days = age * 365
hours = days * 24
seconds = hours * 3600

timeFrame = input("Do you want to know your age in months, days, hours or seconds?")

if timeFrame == "months":
    print(f"{months} months")

elif timeFrame == "days":
    print(f"{days} days")

elif timeFrame == "hours":
    print(f"{hours} hours")

elif timeFrame == "seconds":
    print(f"{seconds} seconds")

else:
    print("Error")