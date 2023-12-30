# Write your solution here
def remove_smallest(numbers: list):

    small = numbers.index(min(numbers))

    numbers.pop(small)
    








if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)