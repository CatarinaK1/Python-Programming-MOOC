def longest_series_of_neighbours(numbers: list) -> int:
    if not numbers:
        return 0

    max_count = 1
    current_count = 1

    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1] + 1 or numbers[i] == numbers[i + 1] - 1:
            current_count += 1
        else:
            current_count = 1

        max_count = max(max_count, current_count)

    return max_count

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
