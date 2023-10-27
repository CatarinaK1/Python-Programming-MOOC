# Please write a program which asks for the user's name. 
#     If the name is anything but "Jerry", 
# the program then asks for the number of portions and prints out 
# the total cost. 
#     The price of a single portion is 5.90.


name = input("Please tell me your name: ")


if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    total = 5.90 * portions
    print(f"The total cost is {total}\n Next please!")

else:
    print("Next please!")





