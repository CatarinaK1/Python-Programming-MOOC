# Write your solution here
def all_the_longest(words: list) -> list:
    #sorted(words, key=len)[0]

    longest_list = []
    longest = 0
    
    for i in words:
        if len(i) > longest:
            longest = len(i)

    

    for j in range(len(words)):
        if len(words[j]) == longest:
            longest_list.append(words[j])

    return longest_list



if __name__ == "__main__":  
    my_list = ['Grace', 'Steve', 'Susan']

    result = all_the_longest(my_list)
    print(result)