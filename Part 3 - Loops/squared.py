#Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters


def squared(text, size):
    a = 0
    for i in range(size):
        print()

        for j in range(size):
            
            if a >= len(text):
                a = 0
            print(text[a],end= '')
            a += 1
            


# Testing the function
if __name__ == "__main__":
    squared("ab",3)