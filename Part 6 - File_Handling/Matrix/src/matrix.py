# write your solution here
def matrix_sum():
    
    Matrix_Sum = 0

    with open("matrix.txt") as matrixFile:
            
        for row in matrixFile:
            
            row = row.replace("\n", "")
            numbers = row.split(",")

            for number in numbers:
                Matrix_Sum += int(number)

  

    return Matrix_Sum


def matrix_max():
         
    with open("matrix.txt") as matrixFile:
        
        Matrix_Max = 0

        for row in matrixFile:
            
            row = row.replace("\n", "")
            numbers = row.split(",")

            for number in numbers:
                if int(number) > Matrix_Max:
                    Matrix_Max = int(number)

    return Matrix_Max

            

def row_sums():
        row_sum_list = []
        with open("matrix.txt") as matrixFile:
            
            for row in matrixFile:
                
                row_number = 0
                row = row.replace("\n", "")
                numbers = row.split(",")

                for number in numbers:

                    row_number += int(number)

                row_sum_list.append(row_number)

        return row_sum_list

# print(row_sums())
# print(matrix_max())
# print(matrix_sum())



