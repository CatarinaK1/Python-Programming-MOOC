# Write your solution here
def no_shouting(words: list) -> list:

    new_list = []

    for i in words:
        if i.isupper() != True:
            new_list.append(i)

    
    return new_list





if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)