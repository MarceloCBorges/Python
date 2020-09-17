# # Ex1
#
# number = [0 for a in range(5)]
#
# for count in range(5):
#     val = int(input('Inform a number: '))
#     number[count] = val
#
#
# print(number)
# # *******************************************************
# # Ex2
# number = [0 for a in range(10)]
#
# for count in range(10):
#     val = int(input('Inform a number: '))
#     number[count] = val
#
# print(number)
# number.sort(reverse=True)
# print(number)
# # *******************************************************
# # Ex3
# grade = [0 for a in range(4)]
# average = 0
#
# for count in range(4):
#     student = float(input('Inform student`s grade: '))
#     grade[count] = student
#
# for count in range(4):
#     print('Student grade: ', grade[count])
#     average += grade[count]
#
# print('Average: ', average / len(grade))
# # *******************************************************
# # Ex4
# size = 5
# number = [0 for c in range(size)]
# pair = []
# odd = []
#
# for count in range(size):
#     val = int(input('Inform number: '))
#     number[count] = val
#     if val % 2 == 0:
#         pair.append(val)
#     else:
#         odd.append(val)
#
# print('Typed numbers: ', number)
# print('Pair numbers: ', pair)
# print('Odd numbers: ', odd)
# # *******************************************************
# # Ex 5
# student = 2
# grade = 6  # name, grade1, grade2, grade3, grade4, average
#
# studentHistory = [[0 for column in range(grade)] for line in range(student)]
#
#
# def show():
#     average_grade = False
#     for namePrint in range(student):
#         if studentHistory[namePrint][grade - 1] < 7:
#             pass
#         else:
#             average_grade = True
#             print('Name: ', studentHistory[namePrint][0])
#
#             for gradePrint in range(1, (grade - 1)):
#                 print(f'Grade {(gradePrint + 1)}: ', (studentHistory[namePrint][gradePrint]))
#
#             print(f'Average: {studentHistory[namePrint][grade - 1]:.2f}')
#             print('**************************************')
#     if average_grade:
#         pass
#     else:
#         print('None of the students achieved the average grade.')
#
#
# def newRecord(student_name):
#     studentHistory[student_name][0] = input('Inform student`s name %d: ' % (student_name + 1))
#     average = 0
#
#     for studentGrade in range(1, (grade - 1)):
#         studentHistory[student_name][studentGrade] = float(input('Inform student`s grade %d: ' % studentGrade))
#         average += studentHistory[student_name][studentGrade]
#
#     studentHistory[student_name][grade - 1] = average / (grade - 2)
#
#
# print('**************************************')
# for studentName in range(student):
#     newRecord(studentName)
# show()
# # *******************************************************
# # Ex 6
# people = 3
# age = 13
# average = 0
# total = 0
#
# population = [[0 for column in range(2)] for line in range(people)]
#
# # age = int(input('Age limit: '))
#
# def newData(data):
#     global average
#
#     population[data][0] = float(input(f'Age of person {data + 1}: '))
#     population[data][1] = float(input(f'Height of person {data + 1} [cm]: '))
#     average += population[data][1]
#
#
# for data in range(people):
#     newData(data)
#
# for dataShow in range(people):
#     if population[dataShow][0] > age and population[data][1] < (average / people):
#         total += 1
#
# print("It was registered %d people(s) under %d that have height lower than average." % (total, age))
# # *******************************************************
# # Ex 7
# val = []
#
#
# def insert():
#     print('To stop the insertion, type any negative number.')
#     input()
#     number = 0
#     while number >= 0:
#         number = int(input('Inform a number: '))
#         if number >= 0:
#             val.append(number)
#
#
# def valTotal():
#     print('Total of numbers informed: ', len(val))
#
#
# def show():
#     print('Numbers informed in normal order:')
#     print(val)
#
#
# def showInverted():
#     print('Numbers informed in inverted order:')
#     val.sort(reverse=True)
#     print(val)
#
#
# def valSum():
#     plus = 0
#
#     for calc in range(len(val)):
#         plus += val[calc]
#
#     return plus
#
#
# def valAverage():
#     average = 0
#
#     for calc in range(len(val)):
#         average += val[calc]
#
#     return average / len(val)
#
#
# def aboveAverage():
#     total = 0
#     for calc in range(len(val)):
#         if val[calc] > valAverage():
#             print(val[calc], end=' ')
#             total += 1
#     print('\nIn a total of {} informed numbers'.format(total))
#
#
# def menu():
#     status = True
#
#     while status:
#         print('1. Insert values.\n'
#               '2. Total value.\n'
#               '3. Show values\n'
#               '4. Show values inverted order.\n'
#               '5. Values sum.\n'
#               '6. Values average.\n'
#               '7. Values above average.\n'
#               '0. Exit')
#         option = int(input())
#
#         if option == 1:
#             insert()
#             print('============================')
#         elif option == 2:
#             valTotal()
#             print('============================')
#         elif option == 3:
#             show()
#             print('============================')
#         elif option == 4:
#             showInverted()
#             print('============================')
#         elif option == 5:
#             print('The average of informed values is: ', valSum())
#             print('============================')
#         elif option == 6:
#             print('The average of informed values is: ', valAverage())
#             print('============================')
#         elif option == 7:
#             print('Numbers above average: ')
#             aboveAverage()
#             print('============================')
#         elif option == 0:
#             status = False
#         else:
#             continue
#
#
# menu()
# # *******************************************************
# student = [[0 for i in range(2)]]
#
# def newLine():
#     line = []
#     for i in range(2):
#         line.append(0)
#     globals.student.append(line)
# (MATRIZ COM COLUNAS DEFINIDAS, PORÉM SEM LINHAS DEFINIDAS
# # Ex 8  INCOMPLETO
# average = 0
#
# athlete = []
#
#
# def insert():
#     global average
#     status = True
#
#     while status:
#         name = input("Athlete name: ")
#         if name == "":
#             status = False
#         else:
#             athlete.append(name)
#             for jmp in range(1, 6):
#                 athlete.append(float(input('Inform jump {}: '.format(jmp))))
#
#     print('*** Final Score ***')
#     print('Athlete name: ', athlete[0])
#     print('Score: ')
#     print(show())
#     print(f'Average: {0:.2f}'.format(average / 5))
#
#
# def show():
#     global average
#     average = 0
#
#     for jmp in range(1, 6):
#         print(jmp)
#         print(athlete)
#         average += athlete[jmp]
#         print(athlete[jmp])
#
#
# def menu():
#     status = True
#
#     while status:
#         print('1. Insert\n'
#               '2. exit')
#         option = int(input())
#
#         if option == 1:
#             insert()
#             print('============================')
#         elif option == 2:
#             status = False
#         else:
#             continue
#
#
# menu()
# # *******************************************************
# Ex 9
# quantity = 0
#
# mouseId = []
# mouseProblem = []
# defect = ('Reading mistakes', 'Cabling problem', 'Button problem', 'Broken')
#
#
# def detailedInfo():
#     global quantity
#
#     print('Detailed Situation:')
#
#     for defect_count in range(len(defect)):
#         print("  " + defect[defect_count] + ':')
#         result = []
#
#         for count in range(quantity):
#             if mouseProblem[count] == defect_count + 1:
#                 result.append(mouseId[count])
#         if len(result) == 0:
#             continue
#         else:
#             print("  ", *result, sep=' - ')
#
#     f'Total devices registered: {quantity}'
#
#
# def info():
#     global quantity
#
#     print('Situation          Quantity     Percentage')
#
#     for defect_count in range(len(defect)):
#         problem_count = 0
#         for count in range(quantity):
#             if mouseProblem[count] == defect_count + 1:
#                 problem_count += 1
#
#         print(defect[defect_count], '   ', problem_count, '   ', (problem_count / quantity) * 100, "%")
#
#     print('Total devices registered: ', quantity)
#
#
# def menu2():
#     status = True
#     while status:
#         print('Would You like to see detailed information?\n'
#               '1. Yes.\n'
#               '2. No')
#         option = int(input())
#
#         if option == 1:
#             detailedInfo()
#             status = False
#         elif option == 2:
#             status = False
#         else:
#             print('Invalid menu option.')
#
#
# def problem():
#     global quantity
#
#     quantity += 1
#
#     print(f'-- Problem found  in {mouseId[quantity - 1]} --')
#     for cnt in range(len(defect)):
#         print(cnt + 1, defect[cnt])
#     # print(f'1. {0}.\n'
#     #       f'2. {1}.\n'
#     #       f'3. {2}.\n'
#     #       f'4. {3}.'.format(defect[0], defect[1], defect[2], defect[3]))
#
#     while True:
#         option = int(input())
#
#         if 0 <= option <= len(defect):
#             return option
#         else:
#             print('Invalid menu option.')
#
#
# def new():
#     status = True
#
#     while status:
#         identification = input('-->Mouse ID: ')
#         if identification == '':
#             status = False
#         else:
#             mouseId.append(identification)
#             mouseProblem.append(problem())
#
#
# def menu():
#     status = True
#
#     while status:
#         print('1. New entry\n'
#               '2. Show data\n'
#               '3. Exit')
#         option = int(input())
#
#         if option == 1:
#             new()
#             print('============================')
#         elif option == 2:
#             info()
#             print('============================')
#             menu2()
#             print('============================')
#         else:
#             print('Invalid menu option.')
#
#
# menu()
# *******************************************************
# # Ex10
# access = {'admin': 'admin', 'user1': 'password1', 'userB': 'passwordB'}
#
# status = True
# while status:
#     user = input('User: ')
#     password = input('Password: ')
#     print()
#     # Check if user exists. If yes, returns with the key
#     if password == access.get(user):
#         print('Successfully logged in.')
#         status = False
#     else:
#         print('User or password incorrect.')
# # *******************************************************
# # Ex 11
# import ex11Module
#
#
# def menu():
#     status = True
#
#     while status:
#         print('1. Show students.\n'
#               '2. Insert a student and grade.\n'
#               '3. Change student grade.\n'
#               '4. Consult student grade.\n'
#               '5. Delete a student.\n'
#               '6. Class average.\n'
#               '7. Change student name.\n'
#               '0. Exit.')
#         option = int(input())
#
#         if option == 1:
#             ex11Module.show()
#             print('============================')
#         elif option == 2:
#             name = input('Inform student\'s name: ')
#             ex11Module.insert(name)
#             print('**Student created successfully.**')
#             print('============================')
#         elif option == 3:
#             ex11Module.change()
#             print('============================')
#         elif option == 4:
#             ex11Module.consult()
#             print('============================')
#         elif option == 5:
#             ex11Module.delete()
#             print('============================')
#         elif option == 6:
#             ex11Module.average()
#             print('============================')
#         elif option == 7:
#             ex11Module.changeName()
#             print('============================')
#         elif option == 0:
#             status = False
#         else:
#             print('Invalid menu option.')
#
#
# menu()
# *******************************************************
# *******************************************************
