# Write your solution here
def list_sum (first_list: list, second_list: list) -> list:

    sum_list = []

    for index in range(len(first_list)):
        sum_list.append(first_list[index] + second_list[index])

   # for value1, value2 in zip(first_list, second_list):
   #     sum_list.append(value1 + value2)


    return sum_list







if __name__ == "__main__":

    first_list = [2,3,4]
    second_list = [2,3,4]

    print(list_sum(first_list, second_list))
 