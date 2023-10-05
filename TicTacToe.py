####Definitons

#Display board
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7],"|",board[8],"|",board[9])
    print(board[4],"|",board[5],"|",board[6])
    print(board[1],"|",board[2],"|",board[3])

#Player Marker
def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1 please choose X or O :").upper()

    if marker == "x":
        return ("X","O")
    else:
        return ("O","X")
    
#Placing marker
def place_marker(board, marker, position):
    board[position] = marker

#Win Con
def win_check(board, mark):
    if board[1]==board[2]==board[3]==mark:
        return True
    elif board[4]==board[5]==board[6]==mark:
        return True
    elif board[7]==board[8]==board[9]==mark:
        return True
    elif board[1]==board[5]==board[9]==mark:
        return True
    elif board[1]==board[4]==board[7]==mark:
        return True
    elif board[2]==board[5]==board[8]==mark:
        return True
    elif board[3]==board[5]==board[7]==mark:
        return True
    elif board[3]==board[6]==board[9]==mark:
        return True
    
#Who first
import random

def choose_first():
    who_first = random.randint(1,2)
    if who_first == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    
#Check if space
def space_check(board, position):
    return board[position] == ' '

#Check if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#Players choice of where to go
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Player please chose a position from 1-9"))
    return position

#Replay Function
def replay():
    play_again = input("Player would you like to play again? yes or no :")
    if play_again == "yes":
        return True
    else:
        return False



### The Game
print('Welcome to Tic Tac Toe!')
while True:

    board = [" "] *10
    player1_marker,player2_marker = player_input()
    who_first = choose_first()
    print (who_first + " will go first!")
    ready_game = input("Are you ready to play? yes or no")
    if ready_game == "yes":
        game_on = True 
    else:
        game_on = False
    while game_on == True:
        if who_first == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)
            if win_check(board,player1_marker):
                display_board(board)
                print("Player 1 has Won! Congratulations")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print ("Its a draw! Better luck next time")
                    game_on = False
                    break
                else:
                    who_first = "Player 2"

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2_marker,position)
            if win_check(board,player2_marker):
                display_board(board)
                print("Player 2 has Won! Congratulations")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print ("Its a draw! Better luck next time")
                    game_on = False
                    break
                else:
                    who_first = "Player 1"
    if not replay():
        break
    