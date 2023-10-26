### **Pre-task**

# Please write a program which asks the user for integer numbers. 
# The program should keep asking for numbers until the user types in zero.
    
# ### **Part 1: Count**
# After reading in the numbers the program should print out how many numbers were typed in. 
# The zero at the end should not be included in the count.
# You will need a new variable here to keep track of the numbers typed in.

# ### Part 2: Sum

# The program should also print out the sum of all the numbers typed in. 
# The zero at the end should not be included in the calculation

# Part 3 : Mean
# The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. 
# You may assume the user will always type in at least one valid non-zero number.

# ### Part 4 : **Positives and negatives**

# The program should also print out statistics on how many of the numbers were positive and how many were negative. 
# The zero at the end should not be included in the calculation.


print("Please type in integer numbers. Type in 0 to finish.")
negative_numbers = 0
positive_numbers = 0
count = 0
number_sum = 0

while True:
    number = int(input("Number: "))
    
    if number == 0:
        break
    elif number < 0:
        negative_numbers += 1
    else:
        positive_numbers += 1
    count += 1
    number_sum += number

mean = number_sum / count

print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {number_sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")