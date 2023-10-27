# Please write a program which asks the user for four numbers. 
# The program then prints out the sum and the mean of the numbers.






sum = 0

for i in range (4):
    number = int(input(f"Number {i + 1}: "))
    sum += number   
    mean = sum / 4 


print(f"The sum of the numbers is {sum} and the mean is {mean}")