# This exercise includes 2 parts
# Part 1: Please write a program which keeps asking the user for words. 
# If the user types in end, the program should print out the story the words formed, and finish.

# Part 2:
# Change the program so that the loop ends also if the user types in the same word twice.

word_list = ""
last_word = ""
while True:
    word = input("Please type in a word:")
    #print(last_word)

    if word == "end":
        break
    #print("The word: ", word)

    if word == last_word:
        break

    word_list += word + " "

    #print("The List", word_list)

    last_word = word

    #print(last_word)


print(word_list)