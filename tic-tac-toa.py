from os import system

board = ['-','-','-',
        '-','-','-',
        '-','-','-']

winner = None

current_player ='X'

game_is_still_on = True

def game_is_still_on():
    if check_if_gameover():
        return False
    else:
        return True

def flip_player(current_player):
    if current_player == 'X':
        return 'O'
    elif current_player == 'O':
        return 'X'

def check_if_gameover():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner == 'X' or row_winner == 'O':
        return True
    elif column_winner == 'X' or column_winner == 'O':
        return True
    elif diagonal_winner == 'X' or diagonal_winner == 'O':
        return True
    else:
        winner = None
    return False
    
def display_board(board):
    for i in range(3):
        print(end='|')
        for j in range(3):
            print(board[i*3+j], end ='|')
        print(end ='\n')

def handle_turn(current_player):
    print("Chose the position from 1 - 9",end='\n')
    position = int(input())
    position = position -1
    board[position]=current_player
    system('clear')
    display_board(board)

def check_rows():
    global game_is_still_on
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        game_is_still_on=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():
    global game_is_still_on
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'
    if col1 or col2 or col3:
        game_is_still_on=False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return

def check_diagonals():
    global game_is_still_on
    dia1 = board[0] == board[4] == board[8] != '-'
    dia2 = board[2] == board[4] == board[6] != '-'
    if dia1 or dia2:
        game_is_still_on=False
    if dia1:
        return board[2]
    elif dia2:
        return board[0]
    return

def play_game():
    global current_player
    display_board(board)
    while game_is_still_on:
        handle_turn(current_player)
        if check_if_gameover():
            return current_player
        current_player = flip_player(current_player)


winner = play_game()
if winner!=None:
    print("The winner is :", winner)
else:
    print("its a tie")




#board
#display board
#play game 
#check win
    #check diagonal
    #check vertical
    #check horizontal
#check loss
#check tie
#flip player