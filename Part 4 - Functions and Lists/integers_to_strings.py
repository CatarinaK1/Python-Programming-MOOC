# Write your solution here
# Write your solution here
def formatted(float_number: list) -> list:
    new_list = []
    formatted_float = 0.0
    
    for i in range(len(float_number)):
        formatted_float = f"{float_number[i]:.2f}"
        new_list.append(formatted_float)

    return new_list








if __name__ == "__main__":
    my_list = [0.123, 1.23, 0.0234]
    new_list = formatted(my_list)
    print(new_list)