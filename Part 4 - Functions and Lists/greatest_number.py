# Write your solution here
def greatest_number(number1, number2, number3):
    
    if number1 > number2 and number1 > number3:
        return number1
    
    elif number2 > number3:
        return number2
    
    else:
        return number3

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)