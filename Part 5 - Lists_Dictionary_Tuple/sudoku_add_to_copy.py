# Write your solution here
import copy


def block_correct(sudoku: list):

    check = []
    
    grid_row = [0,3,6]
    


    for index in grid_row:
        check = []

        for row in sudoku[index : index + 3]:

            for item in row[index : index + 3]:

                check.append(item)
                

        for j in check:
            if check.count(j) > 1 and j != 0:
                return False
            
    
    return True

def column_correct(sudoku: list) -> bool:

    for i in range(len(sudoku)):
        column_count = []
        
        for column in sudoku:

            
            column_count.append(column[i])



        for i in column_count:
            if column_count.count(i) > 1 and i != 0:
                return False
        
    return True

def row_correct(sudoku: list):

    for i in range(len(sudoku)):
    
        for item in sudoku[i]:
            if sudoku[i].count(item) > 1 and item != 0:
                return False
            
    return True

def sudoku_grid_correct(sudoku: list):
    #(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).


    if block_correct(sudoku) == False:
        return False
    
    if column_correct(sudoku) == False:
        return False
    

    if row_correct(sudoku) == False:
        return False


    return True


def print_sudoku(sudoku_example: list):
    
    int_to_string = ""
    count = 0
    row_Count = 0

    for i in range(len(sudoku_example)):

        for item in sudoku_example[i]:


            if item == 0:
                int_to_string += "_"


            if item > 0:
                int_to_string += str(item)

    for element in int_to_string:
        count += 1
        row_Count +=1
        
        print(element, end=" ")
        
        if count % 3 == 0:
            print(" ", end="")
        if row_Count == 9:
            print("\n", end="")
            row_Count = 0

        if count %27  == 0:
            print("\n",end="")

        
def copy_and_add(sudoku_example: list, row_no: int, column_no: int, number: int):

    #sudoku_copy = copy.deepcopy(sudoku)
    sudoku_copy = [row[:] for row in sudoku_example]

    sudoku_copy[row_no][column_no] = number


    return sudoku_copy
    



if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
    
    res = copy_and_add(sudoku, 0, 1, 3)
    print_sudoku(res)
