# Write your solution here
def sum_of_positives(number: list) -> int:
    
    numbers_sum = 0
    
    for i in number:

        if i > 0:
            numbers_sum += i

    return numbers_sum




if __name__ == "__main__":
    print(sum_of_positives((2,-3,4,-7,8,-9,-6)))
    print(sum_of_positives((2,-3, 4,-7,-9,-6)))