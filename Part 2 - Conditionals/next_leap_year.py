# Please write a program which asks the user for a year, and prints out the next leap year.
# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year

year = int(input("Year"))
leap_year = year

while True:

    leap_year += 1

    if leap_year % 100 == 0:
        if leap_year % 400 == 0 :
            break

    elif leap_year % 4 == 0:
        break

print(f"The next leap year after {year} is {leap_year}")