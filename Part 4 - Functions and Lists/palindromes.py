# Write your solution here
def palindromes(word):
    #word = input("Please type in a palindrome:")
   
    for i in range(len(word) ):
        if word[i] == word[-i - 1]:
            status = True


        else:
            status = False
            break
        

    if status:
        print(word,"is a palindrome!")

    else:
        print("that wasn't a palindrome")

        
    return status


def main():
    
    status = False
    while status == False:
        word = input("Please type in a palindrome:")
        status = palindromes(word)

main()

