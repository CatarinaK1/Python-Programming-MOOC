# Write your solution here

phone_book = {}

while True:


    number_Input = int(input("command (1 search, 2 add, 3 quit):"))

    if number_Input == 1:
        name = input("name: ")

        if name in phone_book:
            
            for numbers in phone_book[name]:
     
                print(numbers)

        else:
            print("no number")


    elif number_Input == 2:
        
        name = input("name: ")
        number = input("number: ")

        if name not in phone_book:
            phone_book[name] = []

        phone_book[name].append(number)

        print("ok!")

    elif number_Input == 3:
        print("quitting...")
        break
