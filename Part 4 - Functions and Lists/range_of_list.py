# Write your solution here
def range_of_list(my_list: list) -> int:

    list_max = max(my_list)

    list_min = min(my_list)

    result = list_max - list_min

    return result


# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    #my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print(result)