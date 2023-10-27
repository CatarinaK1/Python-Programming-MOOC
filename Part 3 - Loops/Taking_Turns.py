# Please write a program which asks the user to type in a number. 
# The program then prints out the positive integers between 1 and the number itself, 
# alternating between the two ends of the range as in the examples below.


number = int(input("Please type in a number: "))
turn = 1

while turn + 1 <= number:
    
    print(turn)
    print(number)


    turn += 1
    number -= 1

if turn <= number:
    print(number)