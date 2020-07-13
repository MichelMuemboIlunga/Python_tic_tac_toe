"""
  @developing by Michel Muembo Ilunga
  13/7/2020 at 3:05 AM.
"""
from IPython.display import clear_output
import random


# displaying the game board
def display_board(board):
    clear_output()
    print('  ' + board[7] + ' |  ' + board[8] + '  |  ' + board[9])
    print('-------------')
    print('  ' + board[4] + ' |  ' + board[5] + '  |  ' + board[6])
    print('-------------')
    print('  ' + board[1] + ' |  ' + board[2] + '  |  ' + board[3])


testing_board = ['#', '', '', '', '', '', '', '', '', '']
display_board(testing_board)


# choosing player input
def player_input():
    marker = ''
    while marker != 'x' and marker != 'Y':
        symbol = input('player 1 choose:x or Y: ')

        player_1 = symbol

        if player_1 == 'x':
            player_2 = 'Y'
        else:
            player_2 = 'x'

        return player_1, player_2


player_input()


# displaying the player marker board
def place_marker(board, marker, position):
    board[position] = marker


place_marker(testing_board, '@', 8)
display_board(testing_board)


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


win_check(testing_board, 'X')


# choosing the player
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose The next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe! Are you exiting to go!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('waouh! The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('oups! you loose the challenge!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('oups! Full board The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break








