# Please write a program which estimates a user's typical food expenditure.

# The program asks the user how many times a week they eat at the student cafeteria. 
# Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

# Based on this information the program calculates the user's typical food expenditure both weekly and daily.


# Write your solution here
student_cafeteria_visits = int(input("How many times a week do you eat at the student cafeteria? "))

student_cafeteria_expense = float(input("The price of a typical student lunch?"))

weekly_groceries_expense = float(input("How much money do you spend on groceries in a week?"))


average_weekly_expense =  (student_cafeteria_visits * student_cafeteria_expense) + weekly_groceries_expense

average_daily_expense = average_weekly_expense / 7


print("Average food expenditure")
print(f"Daily: {average_daily_expense} euros")
print(f"Weekly: {average_weekly_expense:.2f} euros")










