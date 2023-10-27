# Please write a program which asks the user for a number of days. 
# The program then prints out the number of seconds in the amount of days given.

day = int(input("How many days?"))

seconds = day * 86400

print(f"Seconds in that many days: {seconds}")