# Write your solution here
def transpose(matrix: list):
    a = [row[:] for row in matrix]
    
    for row in range(len(matrix)):

        for item in range(len(matrix)):
            matrix[row][item] = a[item][row]








if __name__ == "__main__":

    m = [[1,2,3],
        [4, 5, 6],
        [7, 8, 9]
         ]
    
    transpose(m)
    print(m)
    
