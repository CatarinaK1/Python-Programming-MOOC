# Write your solution here
def length_of_longest(words: list) -> int:
    length = 0

    for i in words:
        if len(i) > length:
            length = len(i)

    return length






if __name__ == "__main__":
    
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)