# Write your solution here
def block_correct(sudoku: list):

    check = []
    
    grid_row = [0,3,6]
    grid_column = [0,3,6]



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









if __name__ == "__main__":
    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]]

    print(sudoku_grid_correct(sudoku2))

    sudoku = [
  [ 4, 8, 1, 2, 0, 9, 7, 0, 3 ],
  [ 7, 0, 3, 1, 0, 8, 6, 9, 2 ],
  [ 6, 9, 2, 3, 7, 5, 4, 8, 1 ],
  [ 5, 3, 4, 0, 8, 1, 9, 2, 7 ],
  [ 0, 0, 8, 7, 9, 2, 5, 3, 4 ],
  [ 9, 2, 7, 4, 5, 0, 8, 1, 0 ],
  [ 2, 7, 5, 8, 4, 4, 1, 6, 0 ],
  [ 1, 6, 9, 5, 2, 7, 3, 4, 8 ],
  [ 0, 4, 0, 9, 1, 6, 2, 7, 5 ],
    ]
    print(sudoku_grid_correct(sudoku))