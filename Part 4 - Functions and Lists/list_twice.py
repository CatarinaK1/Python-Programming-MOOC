# Write your solution here
number_list = []

while True:

    user_input = int(input("New item: "))

    if user_input == 0:
        print("Bye!")
        break

    number_list.append(user_input)

    print(f'The list now: {number_list}')
    print(f"The list in order: {sorted(number_list)}")