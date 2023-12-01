# Write your solution here
def first_word(sentence):
    count = 0

    while sentence[count] != " ":

        count += 1
    
    first_word = sentence[0:count]

    return first_word


def second_word(sentence):

    second_word = sentence.split()


    return second_word[1]

def last_word(sentence):

    last_word = sentence.split()

    return last_word[-1]
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))