import os

lines = []


def fileopen():
    global lines

    file = open('../7. Files/File/ex3.txt')
    lines = file.readlines()


def textCheck(line):
    global lines

    file = open('../7. Files/File/ex3.txt')
    lines = file.readlines()
    file.close()

    text = ''
    for c in range(len(lines[line])):
        if not lines[line][c].isnumeric():
            text += lines[line][c]

    aux = int(lines[line][19:]) + 1

    return text + str(aux)


# def write(level, play):
#     global lines
#
#     if level == 'Easy':
#         if int(lines[2][19:]) < play:
#             lines[2] = textCheck(2)
#     elif level == 'Medium':
#         if int(lines[2][19:]) < play:
#             lines[3] = textCheck(3)
#     elif level == 'Hard':
#         if int(lines[2][19:]) < play:
#             lines[4] = textCheck(4)
#     elif level == 'Insane':
#         if int(lines[2][19:]) < play:
#             lines[5] = textCheck(5)
#
#     lines[6] = lines[6] + str(int(lines[6][19:]) + play)
#     file = open('../7. Files/File/ex3.txt', 'w')
#     file.write(str(lines))
#     file.close()
def write(play):
    fileopen()

    actual = ''
    for c in range(len(lines[0][20:])):
        if lines[0][c].isnumeric():
            actual += lines[0][c]

    if actual == '' or actual == 0:
        files = open('../7. Files/File/ex3.txt', 'w')
        files.write('Lower attempt:      ')
        files.write(str(play))
        files.close()
    elif play < actual:
        files = open('../7. Files/File/ex3.txt', 'w')
        files.write('Lower attempt:      ')
        files.write(str(play))
        files.close()


def read():
    global lines

    fileopen()

    for line in range(len(lines)):
        lines[line] = lines[line].rstrip('\n')
        print(lines[line])


def records():
    if os.path.exists('../7. Files/File/ex3.txt'):
        read()
    else:
        filex = open('../7. Files/File/ex3.txt', 'w')
        filex.write('Lower attempt:       ')
    # else:
    #     file = open('../7. Files/File/ex3.txt', 'w')
    #     file.write('__________Record book__________\n')
    #     file.write('    Level         Plays\n')
    #     file.write('--> Easy           0\n'
    #                '--> Medium         0\n'
    #                '--> Hard           0\n'
    #                '--> Insane         0\n'
    #                '** Total games:    0')
    #     file.close()
    #     read()
