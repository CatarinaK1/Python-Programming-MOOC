# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):

    if y < 0 or y >= len(game_board) or x >= len(game_board[0]):
        return False

    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    
    else:
        return False





if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)

    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)
    print(play_turn(game_board, 2, -1, "X"))
    print(game_board)