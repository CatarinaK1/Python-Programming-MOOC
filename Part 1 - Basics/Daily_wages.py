# Please write a program which asks for 
# the hourly wage, hours worked, and the day of the week. 
# The program should then print out the daily wages, 
# which equal hourly wage multiplied by hours worked, 
# except on Sundays when the hourly wage is doubled.


# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
week_day = input("Day of the week: ")

daily_wage = hourly_wage * hours_worked

if week_day == "Sunday":
    daily_wage *= 2
    print(f"Daily wages: {daily_wage} euros")

else:
    print(f"Daily wages: {daily_wage} euros")

    