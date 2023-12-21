# Write your solution here
def shortest(words: list) -> str:
    #sorted(words, key=len)[0]

    shortest = words[0]
    # longest = words[0]

    # for i in words:
    #     if len(i) > len(shortest):
    #        longest = i

    #        for j in range(len(words)):
    #             if len(shortest) > len(words[j]):
    #                 shortest = words[j]

    for j in range(len(words)):
        if len(shortest) > len(words[j]):
            shortest = words[j]


    #print(longest)
    #print(shortest)
    return shortest
        




if __name__ == "__main__":  
    my_list = ["first", "second", "fourth", "eleventh"]

    #result = shortest(my_list)
    #print(result)
    shortest(my_list)