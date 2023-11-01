# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    player = "X"
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print (board)
        # TODO: Input a move from the player.
        x, y = input("Enter the postition(x,y), split with ',':").split(",")
        # TODO: Update the board.
        board[int(x)][int(y)] = player
        winner = get_winner(board)
        # TODO: Update who's turn it is.
        if not winner:
            player = other_player(player)
        print(winner)
