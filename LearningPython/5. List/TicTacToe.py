board = []


def newGame():
    global board
    board = [[0 for col in range(3)] for lin in range(3)]
    show()
    play()


def show():
    print()
    for line in range(3):
        for column in range(3):
            if board[line][column] == 1:
                print(' ', 'x', end=' ')
            elif board[line][column] == -1:
                print(' ', 'O', end=' ')
            else:
                print(' ', '-', end=' ')
        print()


def winner():
    for column in range(3):
        result = board[0][column] + board[1][column] + board[2][column]
        if result == 3 or result == -3:
            return 1

    for line in range(3):
        result = board[line][0] + board[line][1] + board[line][2]
        if result == 3 or result == -3:
            return 1

    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0


def play():
    player = 1
    rounds = 0
    move = 1
    while winner() == 0:
        print()
        print('Player', player, '. Make your move:')
        line = int(input('Line: '))
        if line == 1 or line == 2 or line == 3:
            column = int(input('Column: '))
            if column == 1 or column == 2 or column == 3:
                if board[line - 1][column - 1] == 0:
                    board[line - 1][column - 1] = move
                    show()
                    if winner():
                        print()
                        print('*********************************************\n'
                              'Congratulations player', player, 'you won this game.\n'
                                                                '*********************************************')
                        print()
                        menu()
                    else:
                        rounds += 1
                        if rounds == 9:
                            print('**********************************\n'
                                  'The game ended in a draw.\n'
                                  '**********************************')
                            print()
                            menu()
                        else:
                            player += 1
                            move = -1
                            if player > 2:
                                player = 1
                                move = 1
                else:
                    print('ALERT!: Cannot insert your move.\n'
                          'This field it is not empty.\n')
            else:
                print('Column does not exist.')
        else:
            print('Line does not exist.')

    menu()


def menu():
    status = True

    while status:
        print('1. New Game\n'
              '2. Exit')
        option = int(input())

        if option == 1:
            newGame()
        elif option == 2:
            print('See you next time.')
            status = False


print('***Welcome to TIC TAC TOE***')
menu()
