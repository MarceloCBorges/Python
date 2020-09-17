# # ex1
# grade = 1
# while grade != 0:
#     grade = float(input('Inform the student`s grade:'))
#     if 0 <= grade > 10:
#         print('Incorrect grade. Inform a number between 0.1 and 10.')
#         continue
#     print('Student grade: ', grade)
# # ------------------------------------------------------------------------
# # ex2
# user = input('User name: ')
# password = input('Password: ')
# error = True
#
# while error:
#     if user == password:
#         print('User and password cannot be the same.')
#         user = input('User name: ')
#         password = input('Password: ')
#     else:
#         error = False
#
# print('User name: ', user)
# print('Password: ', password)
# # ------------------------------------------------------------------------
# # ex3
# popA = int(input('Country A population: '))
# growA = float(input('Growth rate country A[%]: '))
# popB = int(input('Country B population: '))
# growB = float(input('Growth rate country B[%]: '))
# growA = growA / 100
# growB = growB / 100
#
# year = 0
#
# while popA < popB:
#     popA = popA + popA * growA
#     popB = popB + popB * growB
#     year += 1
#
# print('It will take %d year(s) to country A reach the country B population.' % year)
# print(f'Country A population: {popA:.2f}')
# print(f'Country B population: {popB:.2f}')
# # ------------------------------------------------------------------------
# # ex4
# addition = 0
# num = float(input('Type number %d:' % 1))
# high = num
# addition += num
#
#
# for count in range(4):
#     num = float(input('Type number %d:' % (count + 2)))
#     addition += num
#     if num > high:
#         high = num
#
# average = addition / 5
# print('Sum: ', addition)
# print('High: ', high)
# print('Average: ', average)
# # ------------------------------------------------------------------------
# # ex5
# for count in range(49):
#     if not count % 2 == 0:
#         print(count, end=' ')
# # ------------------------------------------------------------------------
# # ex6
# n1 = int(input('Inform the beginning of list: '))
# n2 = int(input('Inform the end of list: '))
#
# for count in range(n1, n2+1):
#     print(count, end=' ')
# # ------------------------------------------------------------------------
# # ex7
# value = int(input('Input the multiplication table value: '))
#
# for multi in range(11):
#     print(multi, '*', value, ' = ', value * multi)
# # ------------------------------------------------------------------------
# # ex8
# odd = 0
# even = 0
#
# for count in range(10):
#     number = int(input('Inform number %d:' % (count + 1)))
#     if number % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print('Even numbers: ', even)
# print('Odd numbers: ', odd)
# # ------------------------------------------------------------------------
# ex9
# fiboTerm = int(input('Inform term of Fibonacci Sequence: '))
#
# elementA = 0
# elementB = 1
#
# if fiboTerm == 1 or fiboTerm == 2:
#     print('Fibonacci sequence fo element ', fiboTerm, 'is: 1')
# else:
#     term = 2
#     while term <= fiboTerm:
#         number = elementA + elementB
#         elementA = elementB
#         elementB = number
#         term += 1
#
#     print('Fibonacci sequence fo element ', fiboTerm, 'is: ', number)
# # ------------------------------------------------------------------------
# # ex10
# total = int(input('Total of age to input: '))
# average = 0
#
# for count in range(total):
#     age = int(input('Inform age %d: ' % (count + 1)))
#     average += age
#
# average = average / total
#
# if 0 < average <= 25:
#     print('Young group.')
# elif 26 < average <= 60:
#     print('Adult group.')
# else:
#     print('Senior group.')
# # ------------------------------------------------------------------------
# # ex11
# item = 1
# add = 0
#
# while True:
#     price = float(input('Product %d: $' % item))
#     add += price
#     if price == 0:
#         print('Total: $', add)
#         payment = float(input('Money: $'))
#         print(f'Exchange: ${(payment - add):.2f}', )
#         print('Would you like to register next shop?\n'
#               '1. Yes\n'
#               '2. No')
#         menu = int(input())
#         if menu == 1:
#             item = 1
#             add = 0
#         else:
#             break
#     else:
#         item += 1
# # ------------------------------------------------------------------------
# # ex12
# multiplier = int(input('Input the multiplication table value: '))
# begin = int(input('Inform the start of multiplication table: '))
# end = int(input('Inform the end of multiplication table: '))
# end += 1
#
# for table in range(begin, end):
#     print(table, '*', multiplier, ' = ', table*multiplier)
# # ------------------------------------------------------------------------
# # ex13
# studentId = int(input('Student ID: '))
# grade = float(input('Student grade: '))
# highId = studentId
# highGrade = grade
#
# lowId = studentId
# lowGrade = grade
#
# for grade in range(9):
#     studentId = int(input('Student ID: '))
#     grade = float(input('Student grade: '))
#     if grade > highId:
#         highId = studentId
#         highGrade = grade
#     elif grade < lowId:
#         highId = studentId
#         highGrade = grade
#
# print('Student with highest grade: ', highId, ' with the grade of ', highGrade)
# print('Student with lowest grade: ', lowId, ' with the grade of ', lowGrade)
# # ------------------------------------------------------------------------
# # ex14
# g1 = 0
# g2 = 0
# g3 = 0
# g4 = 0
# number = 0
#
# while number >= 0:
#     number = int(input('Inform a number--> '))
#     if 0 < number <= 25:
#         g1 += 1
#     elif 26 < number <= 50:
#         g2 += 1
#     elif 51 < number <= 75:
#         g3 += 1
#     elif 71 < number <= 100:
#         g4 += 1
#
# print('You inform %d number between 0 and 25.' % g1)
# print('You inform %d number between 26 and 50.' % g2)
# print('You inform %d number between 51 and 75.' % g3)
# print('You inform %d number between 76 and 100.' % g4)
# # ------------------------------------------------------------------------
# ex15
# total = 0
# order = False
# status = True
#
# name = input('Seller name: ')
#
# print('Hello ', name)
#
# while status:
#     print('Please, choose an option:\n'
#           '1. Order\n'
#           '2. Exit')
#     option = int(input())
#     if 1 < option > 2:
#         print('Invalid option.')
#     elif option == 1:
#         order = True
#     else:
#         status = False
#
#     while order:
#         print('-----------------------------')
#         print('         *****Menu*****  \n'
#               'Product       Code   Price\n'
#               'Hot dog       100    $ 2.39\n'
#               'Hamburguer    101    $ 4.69\n'
#               'Donut         102    $ 0.99\n'
#               'Sandwich      103    $ 3.79\n'
#               'Hot chocolate 104    $ 1.76\n'
#               'Close order   105')
#         print('-----------------------------')
#         menu = int(input('Product code: '))
#         if 100 < menu > 105:
#             print('Invalid code.')
#             continue
#
#         if menu == 100:
#             price = 2.39
#             quantity = int(input('Quantity: '))
#             if quantity == 0:
#                 print('Invalid value.')
#                 continue
#             else:
#                 total += (quantity * price)
#         elif menu == 101:
#             price = 4.69
#             quantity = int(input('Quantity: '))
#             if quantity == 0:
#                 print('Invalid value.')
#                 continue
#             else:
#                 total += (quantity * price)
#         elif menu == 102:
#             price = 0.99
#             quantity = int(input('Quantity: '))
#             if quantity == 0:
#                 print('Invalid value.')
#                 continue
#             else:
#                 total += (quantity * price)
#         elif menu == 103:
#             price = 3.79
#             quantity = int(input('Quantity: '))
#             if quantity == 0:
#                 print('Invalid value.')
#                 continue
#             else:
#                 total += (quantity * price)
#         elif menu == 104:
#             price = 1.76
#             quantity = int(input('Quantity: '))
#             if quantity == 0:
#                 print('Invalid value.')
#                 continue
#             else:
#                 total += (quantity * price)
#         elif menu == 105:
#             print(f'Total: ${total:.2f}')
#             payment = float(input('Money: $'))
#             print(f'Exchange: ${(payment - total):.2f}')
#             print('Thank you to buy with us. Come back soon')
#             print('***********************************')
#             order = False
# ------------------------------------------------------------------------
# # ex16
# candidate1 = 0
# candidate2 = 0
# candidate3 = 0
# candidate4 = 0
# null = 0
# percentageNull = 0
# blank = 0
# percentageBlank = 0
# total = 0
# vote = 1
#
# while vote != 0:
#     print('Candidate  Code\n'
#           ' 1           1\n'
#           ' 2           2\n'
#           ' 3           3\n'
#           ' 4           4\n'
#           ' Null        5\n'
#           ' Blank vote  6\n')
#     vote = int(input('Vote: '))
#
#     if vote == 1:
#         total += 1
#         candidate1 += 1
#     elif vote == 2:
#         total += 1
#         candidate2 += 1
#     elif vote == 3:
#         total += 1
#         candidate3 += 1
#     elif vote == 4:
#         total += 1
#         candidate4 += 1
#     elif vote == 5:
#         total += 1
#         null += 1
#         percentageNull = null / total
#     elif vote == 6:
#         total += 1
#         blank += 1
#         percentageBlank = blank / total
#     elif vote > 6:
#         print('Invalid option.')
#
# print('Candidate 1 with a total of ', candidate1, ' votes.')
# print('Candidate 2 with a total of ', candidate2, ' votes.')
# print('Candidate 3 with a total of ', candidate3, ' votes.')
# print('Candidate 4 with a total of ', candidate4, ' votes.')
# print('Null votes:', null, f'. Percentage: {(percentageNull* 100):.2f}%')
# print('Blank votes:', blank, f'. Percentage: {(percentageBlank* 100):.2f}%')
# # ------------------------------------------------------------------------
# # ex17
#
# athlete = input('Athlete name: ')
#
# score = float(input("Score 1: "))
# total = score
# high = score
# low = score
#
# for jury in range(6):
#     score = float(input("Score %d: " % (jury + 2)))
#     total += score
#     if score > high:
#         high = score
#     elif score < low:
#         low = score
#
# total = total-high-low
# print('Final result: ')
# print('Athlete: ', athlete)
# print(f'Best score: {high:.1f}\n'
#       f'Lowest score: {low:.1f}\n'
#       f'Average score: {(total/5):.2f}')
# # ------------------------------------------------------------------------
# Desafio
# ------------------------------------------------------------------------
