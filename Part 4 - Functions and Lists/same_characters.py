# Write your solution here
def same_chars(text, index1, index2):

    if index1 >= len(text) or index2 >= len(text):
        return False

    if text[index1] == text[index2]:
        return True
    
    else:
        return False



# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("abc", 1, 3))