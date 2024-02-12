# Write your solution here
def histogram(word: str)-> dict:
    
    letters_Hist = {}

    for letter_index in range (len(word)):

        if word[letter_index] not in letters_Hist:
            letters_Hist[word[letter_index]] = "*"

        else:
            letters_Hist[word[letter_index]] += "*"

    for key, value in letters_Hist.items():
        print(f"{key} {value}")





if __name__ == "__main__":

    histogram("abba")


    histogram("statistically")
 