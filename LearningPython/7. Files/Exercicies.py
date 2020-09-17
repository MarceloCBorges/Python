# # Ex1
# def write():
#     file = open('../7. Files/File/ex1.txt', 'a')
#     file.write(input('* Inform text to insert in the file: ') + '\n')
#     file.close()
#
#
# def read():
#     file = open('../7. Files/File/ex1.txt')
#     lines = file.readlines()
#     if len(lines) == 0:
#         print('--> File is empty.')
#     else:
#         print('----------------------------')
#         for line in lines:
#             line = line.rstrip('\n')
#             print(line)
#
#
# def menu():
#     status = True
#     while status:
#         print('What would you like to do?')
#         print('1. Write file\n'
#               '2. Read file\n'
#               '3. Exit')
#         option = int(input())
#
#         if option == 1:
#             write()
#             print('----------------------------')
#         elif option == 2:
#             read()
#             print('----------------------------')
#         elif option == 3:
#             status = False
#         else:
#             menu()
#
#
# menu()
# # print('********************************************************')
# # Ex2
# import os
#
# lines = []
# totalSpace = 0
#
#
# def read():
#     global lines, totalSpace
#
#     file = open('../7. Files/File/userEx2.txt')
#     lines = file.readlines()
#
#     for line in range(len(lines)):
#         lines[line] = lines[line].rstrip('\n')
#         totalSpace = int(lines[line][16:]) + totalSpace
#
#     totalSpace = totalSpace / 1048576
#
#
# def megabyte(lin):
#     #  1 Megabyte  = 1048576 Bytes (in binary)
#     return int(lines[lin][16:]) / 1048576
#
#
# def fillup():
#     files = open('../7. Files/File/ex2.txt', 'a')
#
#     files.write('Nr    User            Use       %\n')
#     for line in range(len(lines)):
#         mega = megabyte(line)
#         text = str(f'{line + 1}   {lines[line][:15]}   {mega:.2f} Mb   {((mega / totalSpace) * 100):.2f}%\n')
#         files.write(text)
#
#     files.write(f'--> Total in use: {totalSpace:.2f} MB\n')
#     files.write(f'--> Average per user: {(totalSpace / len(lines)):.2f} MB\n')
#     print('File written with success')
#     files.close()
#
#
# def write():
#     if os.path.exists('../7. Files/File/ex2.txt'):
#         fillup()
#     else:
#         os.makedirs('../7. Files/File/ex2.txt')
#         print('File does not exists..')
#         print('File created with success.')
#         fillup()
#
#
# read()
# write()
# # print('********************************************************')
# Ex3
import Ex3ModuleGame
import Ex3ModuleFile


def menu():
    status = True
    while status:
        print('1. New game\n'
              '2. Rules\n'
              '3. Records\n'
              '4. Exit')
        option = int(input())
        if option == 1:
            Ex3ModuleGame.newgame()
        elif option == 2:
            Ex3ModuleGame.rules()
            print('-----------------------')
        elif option == 3:
            Ex3ModuleFile.records()
            print('-----------------------')
        elif option == 4:
            status = False
        else:
            menu()


print('**Welcome to try to guess**')
menu()
