#from IPython.display import clear_output #para borrar diferentes tictac boards para que no este mostrando todos
#no se porq no me toma clear_output (creo q solo sirve para jupyter)

# primero hago el tablero
test_board = ['','X','O','X','O','X','O','X','O','X'] #lo uso nada mas para chequear en los pasos previos al juego completo 
def display_board(board):
    #clear_output()
    print(' ' + '|' + ' ' + '|' + ' ')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(' ' + '|' + ' ' + '|' + ' ')
    print('-|-|-')
    print(' ' + '|' + ' ' + '|' + ' ')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(' ' + '|' + ' ' + '|' + ' ')
    print('-|-|-')
    print(' ' + '|' + ' ' + '|' + ' ')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(' ' + '|' + ' ' + '|' + ' ')



#segundo pregunto que quiere ser el jugador 1

# def player_input():
#     marker = ''
#     while marker != 'X' and marker != 'O':
#         marker = input('Jugador 1, por favor elija X o O para empezar: ').upper()
#         print('Disculpe, no se pudo empezar porque no eligio X o O')
#     player1 = marker
#     if player1 == 'X':
#         player2 = 'O'
#     else:
#         player2 = 'X'
#     return (player1,player2)

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Jugador 1, por favor elija X o O para empezar: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



#tercero pregunto donde quiere poner el choice (1-9)
# def player_marker(board, marker):
#     position = ''
#     while position != range(1,9):
#         position = int(input('Por favor elija su siguiente movimiento (1-9): '))
#         if position not in range(1,9):
#             print('Lo lamento, no se pudo completar su movimiento!')
#             position = int(input('Por favor elija su siguiente movimiento (1-9): '))
#         else:
#             break

#     board[position] = marker



def player_marker(board,marker,position):
    board[position] = marker


#chequear si gano 
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# win_check(test_board,'X')

#Que el jugador del principio sea al azar
import random 
# def jugador_que_empieza():
#     if random.randint(0 , 1) == 0:
#         return print('Player 1')
#     else:
#         return print('Player 2')

def jugador_que_empieza():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#fijarse si el lugar esta vacio en board 
def lugar_vacio(board, position):
    return board[position] == ' '

#fijarse si board == full
# def board_full(board):
#     if ' ' not in board[1:10]:
#         return 'Game Over!' 
#     else:
#         return board

def board_full(board):
    for i in range(1,10):
        if lugar_vacio(board,i):
            return False
    return True

#player choice
def player_choice(board):
    position = 0
    while position not in range(1,10) or not lugar_vacio(board, position):
        position = int(input('Por favor elija su siguiente movimiento (1-9): '))
    return position

#preguntar si quieren jugar de nuevo
def replay():
    return input('Queres jugar de nuevo? Escriba Si o No: ').lower().startswith('s')


#el juego en si 
while True:
    the_board = [' ']*10
    turno = jugador_que_empieza()
    player1_marker, player2_marker = player_input()
    print(f'{turno} le toca empezar')

    jugar = input('Queres empezar a jugar? Si o No: ')
    if jugar.lower()[0] == 's':
        game_on = True
    else:
        game_on = False
    while game_on == True:
        if turno == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            player_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print(f'Felicitaciones {turno}! Ganaste!')
                game_on = False
            else:
                if board_full(the_board):
                    display_board(the_board)
                    print('Empate!')
                    break
                else:
                    turno = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            player_marker(the_board, player2_marker, position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print(f'Felicitaciones {turno}! Ganaste!')
                game_on = False 
            else:
                if board_full(the_board):
                    display_board(the_board)
                    print('Empate!')
                    break
                else:
                    turno = 'Player 1'
    if not replay():
        break