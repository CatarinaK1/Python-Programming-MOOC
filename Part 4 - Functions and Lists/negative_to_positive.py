# Write your solution here

# Please write a program which asks the user for a positive integer N. 
# The program then prints out all numbers between -N and N inclusive, 
# but leaves out the number 0. Each number should be printed on a separate line.

number = int(input("Please type in a positive integer:"))

#number = 4


for i in range(-number, number + 1):
    
    if i != 0:
        print(i)