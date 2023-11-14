# Copy here code of line function from previous exercise and use it in your solution
def line(number, text):
    
    if text == "":
        print('*' * number)

    else:
        print(text[0] * number)

    
def triangle(triangle_height, triangle_symbol):
    count = 1

    while count <= triangle_height:
        line( count, triangle_symbol)
        count += 1


def rectangle(triangle_height,square_size,square_symbol):

    for i in range (square_size):
        line(triangle_height,square_symbol)



def shape(triangle_height, triangle_symbol, square_size, square_symbol):

    triangle(triangle_height, triangle_symbol)
    rectangle(triangle_height, square_size,square_symbol)

# You can test your function by calling it within the following block 
if __name__ == "__main__":
    #shape(5, "x", 2, "o")
    shape(5, "X", 3, "*") 
