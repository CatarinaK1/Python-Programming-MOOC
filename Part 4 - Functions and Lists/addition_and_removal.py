# Write your solution here
# The list is now []
# a(d)d, (r)emove or e(x)it: d
# The list is now [1]
# The item that is added must always be one greater than the last item in the list. T
# The first item to be added must be 1.

final_list = []
print(f"The list is now {final_list}")

while True:
    user_input = input("a(d)d, (r)emove or e(x)it:")

    if user_input == 'd' and len(final_list) == 0:
        final_list.append(1)

    elif user_input == 'd':
        final_list.append(final_list[-1] + 1)
    
    elif user_input == 'r':
        final_list.pop(-1)
    
    elif user_input == 'x':
        print('Bye!')
        break

    else:
        break

    print(f"The list is now {final_list}")
