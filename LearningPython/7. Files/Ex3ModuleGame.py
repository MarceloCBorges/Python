import random

import Ex3ModuleFile


levelGame = ''


# def level():
#     global levelGame
#
#     print('Choose your level:\n'
#           '1. Easy\n'
#           '2. Medium\n'
#           '3. Hard\n'
#           '4. Insane')
#     levels = int(input())
#
#     if levels == 1:
#         levelGame = 'Easy'
#         return 10
#     elif levels == 2:
#         levelGame = 'Medium'
#         return 100
#     elif levels == 3:
#         levelGame = 'Hard'
#         return 1000
#     elif levels == 4:
#         levelGame = 'Insane'
#         return 10000
#     else:
#         print('Incorrect level.\n')
#         level()


def newgame():
    # play(generate(level()))
    play(generate(10))


def generate(maximum):
    return random.randint(1, maximum)


def play(number):

    plays = 0
    status = True

    while status:
        guess = int(input('Try to find the number that I chose: '))
        plays += 1

        if guess > number:
            print('Try again.. My number is lower than %d.' % guess)
        elif guess < number:
            print('Try again.. My number is higher than %d.' % guess)
        else:
            print('*********************************************\n'
                  'Congratulations.. You find my secret number.\n'
                  'You did it in %d plays.\n'
                  '*********************************************' % plays)
            # Ex3ModuleFile.write(levelGame, plays)
            Ex3ModuleFile.write(plays)
            status = False


def rules():
    print('*********************************************\n'
          'Game rules:\n'
          '1. Choose the game level.\n'
          '2. A random number will be selected.\n'
          '3. Try to guess what the number it is.\n'
          '4. Will be informed if the number is higher or lower than your guess.\n'
          '*********************************************')
