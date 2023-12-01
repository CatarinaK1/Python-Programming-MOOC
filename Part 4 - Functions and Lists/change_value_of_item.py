
numbers = [1, 2, 3, 4, 5]
index = 0

while True:

    index = int(input("Index: "))
    
    if index < 0:
        break

    new_number = int(input("New value: "))

    numbers[index] = new_number

    print(numbers)

