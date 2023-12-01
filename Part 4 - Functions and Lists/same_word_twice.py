# Write your solution here

word_list = []

while True:

    given_word = input("Word: ")

    if given_word in word_list:
        break

    word_list.append(given_word)

print(f"You typed in {len(word_list)} different words")