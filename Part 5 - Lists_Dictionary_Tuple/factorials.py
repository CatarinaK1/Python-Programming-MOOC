# Write your solution here
def factorials(n: int)-> dict:
    factorial_dict = {}

    for item in range(1, n + 1):
        
        num = item
        res = 1

        while num != 0:
            

            res *= num
            num -= 1


            

        factorial_dict [item] = res

    return factorial_dict







if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])

    k = factorials(1)
    print(k[1])