# Write your solution here
# You can test your function by calling it within the following block
def spruce(height):

    print('a spruce!')
    space = height -1
    row = space - 1
    count = 1


    while space >= 0:

        print(" " * space, end = '')
        print('*' * (2 * count - 1))
        count += 1
        space -=1   

    print(" " * row,'*')



if __name__ == "__main__":
    spruce(5)
