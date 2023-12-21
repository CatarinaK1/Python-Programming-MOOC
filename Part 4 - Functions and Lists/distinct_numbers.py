# Write your solution here
def distinct_numbers(numbers: list) -> list:

    distinct = []

    for i in numbers:
        if i not in distinct:
            distinct.append(i)
            distinct.sort()

    return distinct


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]