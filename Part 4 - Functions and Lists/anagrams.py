
def anagrams(word1, word2):


    if sorted(word1) == sorted(word2):
                
        return True

    else:
        return False


if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False