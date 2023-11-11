#Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. 
#The function takes an integer argument, which specifies the length of the side of the board.


def chessboard(size):



    for i in range(size):
        print()

        for j in range(size):
            if (j + i) % 2 == 0:
                print('1',end= '')

            else:    
                print('0',end= '')
        



# Testing the function
if __name__ == "__main__":
    chessboard(3)
