import ChallengeModule


def menu():
    status = True
    while status:
        print('1. New game\n'
              '2. Rules\n'
              '3. Exit')
        option = int(input())
        if option == 1:
            ChallengeModule.newgame()
        elif option == 2:
            ChallengeModule.rules()
        elif option == 3:
            status = False
        else:
            menu()


print('**Welcome to try to guess**')
menu()
