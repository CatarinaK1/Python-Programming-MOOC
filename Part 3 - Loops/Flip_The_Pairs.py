# Please write a program which asks the user to type in a number. 
# The program then prints out all the positive integer values from 1 up to the number. 
# However, the order of the numbers is changed so that each pair or numbers is flipped. 
# That is, 2 comes before 1, 4 before 3 and so forth.


number = int(input("Please type in a number: "))
pair = 1

while True:
    
    if pair == number:
        print(pair)
        break
    
    if pair > number:
        break

    print(pair + 1)
    print(pair)
    pair += 2

    