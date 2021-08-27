import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def insert_letter(letter, position):
    board[position] = letter


def is_space_free(position):
    return board[position] == ' '


def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def is_winner(board, letter):
    return (board[0] == letter and board[1] == letter and board[2] == letter) or (board[3] == letter and board[4] == letter and board[5] == letter) or (board[6] == letter and board[7] == letter and board[8] == letter) or (board[0] == letter and board[3] == letter and board[6] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[0] == letter and board[4] == letter and board[8] == letter) or (board[2] == letter and board[4] == letter and board[6] == letter)


def is_board_full(board):
    return board.count(' ') == 0


def player_move():
    is_playing = True

    while is_playing:
        position = int(input('Select your position:'))

        if 0 <= position < 9:
            if is_space_free(position):
                insert_letter('X', position)
                is_playing = False
            else:
                print('Space is not free, try again')
        else:
            print('Bad value given, try again')


def computer_move():
    is_playing = True
    while is_playing:
        position = random.randint(0, 8)
        if is_space_free(position):
            insert_letter('O', position)
            is_playing = False


def main():
    print('🧑‍💻 Welcome to Tic Tac Toe!')

    while not is_board_full(board):
        print('Computer plays')
        computer_move()
        print_board(board)
        if is_winner(board, 'O'):
            print('You lost... 😞')
            break

        player_move()
        print_board(board)

        if is_winner(board, 'X'):
            print('You won! 🎉')
            break

    if is_board_full(board):
        print('This is a tie!')


main()

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y':
        main()
    else:
        print('👋🏻 Bye!')
        break
