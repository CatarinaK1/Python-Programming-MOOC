def line(number, text):
    
    if text == "":
        print('*' * number)

    else:
        print(text[0] * number)

def triangle(size):
    # You should call function line here with proper parameters
    count = 1
    while count <= size:
        line( count,"#")
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
