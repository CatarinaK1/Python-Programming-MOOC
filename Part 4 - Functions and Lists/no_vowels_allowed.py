# Write your solution here
def no_vowels(word: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowel_word = word
    
    for i in vowels:

        if i in no_vowel_word:
            no_vowel_word = no_vowel_word.replace(i, "")

    return no_vowel_word



if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))