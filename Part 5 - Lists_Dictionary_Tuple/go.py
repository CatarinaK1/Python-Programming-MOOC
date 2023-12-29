# Write your solution here
def who_won(game_board: list):
    
    player1_score = 0
    player2_score = 0
    
    for row in game_board:
        for item in row:
            if item == 1:
                player1_score += 1

            if item == 2:
                player2_score += 1


    if player1_score == player2_score:
        return 0
    elif player1_score > player2_score:
        return 1
    
    else:
        return 2






if __name__ == "__main__":
    game = [[0,2,1], [2,2,1], [1,0,2],[2,0,0]]

    winner = who_won(game)
    print(winner)
