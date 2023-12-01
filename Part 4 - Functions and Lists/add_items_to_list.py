# Write your solution here


item_list = []

number = int(input('How many items:'))

for i in range(number):
    add_item = int(input(f'Item {i+1}: '))

    item_list.append(add_item)

print(item_list)