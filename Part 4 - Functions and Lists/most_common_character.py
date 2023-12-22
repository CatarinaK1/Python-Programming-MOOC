# Write your solution here
def most_common_character(word: str) -> chr:
    count = 0
    most_char = ""
    
    for i in word:
        if word.count(i) > count:
            count = word.count(i)
            most_char = i

    return most_char





if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))