# Write your solution here
def even_numbers(numbers: list) -> list:
    
    even_Numbers_List = []    
    
    for i in numbers:
        if i % 2 == 0:
            even_Numbers_List.append(i)

    return even_Numbers_List








if __name__ == "__main__":

    number = [1, 2, 3, 4, 5]
    print(even_numbers(number))

    print(even_numbers((4,6,8,9, 56, 87,43, 65)))