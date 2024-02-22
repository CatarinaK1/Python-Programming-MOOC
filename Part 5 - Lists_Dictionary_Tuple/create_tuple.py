# Write your solution here
def create_tuple(x: int, y: int, z: int)-> tuple:

    numbers_tuple = (x, y, z)

    arguments_sum = sum(numbers_tuple)
    biggest = max(numbers_tuple)
    smallest = min(numbers_tuple)

    result = (smallest, biggest, arguments_sum)

    return result









if __name__ == "__main__":
    print(create_tuple(5,3,-1))
    print(create_tuple(1,4,2))


