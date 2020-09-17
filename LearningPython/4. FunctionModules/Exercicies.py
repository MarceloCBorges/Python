# # Ex1
# def FahrenheitCelsius(temperature):
#     print('Fahrenheit: ', temperature)
#     print('Celsius: ', ((temperature - 32) * 5 / 9))
#     print('******************')
#
#
# def CelsiusFahrenheit(temperature):
#     print('Celsius: ', temperature)
#     print('Fahrenheit: ', ((temperature * 9 / 5) + 32))
#     print('******************')
#
#
# def menu():
#     option = 1
#     while option != 0:
#         print('Choose an option: ')
#         print('1. Celsius to Fahrenheit\n'
#               '2. Fahrenheit to Celsius\n'
#               '0. Exit')
#         option = int(input())
#
#         if option == 1:
#             temperature = float(input('Celsius temperature: '))
#             CelsiusFahrenheit(temperature)
#         elif option == 2:
#             temperature = float(input('Fahrenheit temperature: '))
#             FahrenheitCelsius(temperature)
#         elif option == 0:
#             pass
#         else:
#             continue
#
#
# menu()
# # ***********************************************************
# Ex2
# high = 0
# low = 0
#
#
# def highest(num):
#     global high
#     if num > high:
#         high = num
#
#
# def lowest(num):
#     global low
#     if num < low:
#         low = num
#
#
# val = float(input('Inform number: '))
# high = val
# low = val
#
# for num in range(2):
#     val = float(input('Inform number: '))
#     highest(val)
#     lowest(val)
#
# print('Highest number: ', high)
# print('Lowest number: ', low)
# # ***********************************************************
# Ex3
# import random
#
# freq1 = freq2 = freq3 = freq4 = freq5 = freq6 = 0
# launch = 1000
#
#
# def generate():
#     number = random.randint(1, 6)
#     return number
#
#
# def frequency(number):
#     global freq1, freq2, freq3, freq4, freq5, freq6
#     if number == 1:
#         freq1 += 1
#     elif number == 2:
#         freq2 += 1
#     elif number == 3:
#         freq3 += 1
#     elif number == 4:
#         freq4 += 1
#     elif number == 5:
#         freq5 += 1
#     elif number == 6:
#         freq6 += 1
#
#
# for count in range(launch):
#     frequency(generate())
#
# print('Number frequency table: ')
# print('   Number   Frequency\n'
#       '     1        ', freq1, '\n'
#       '     2        ', freq2, '\n'
#       '     3        ', freq3, '\n'
#       '     4        ', freq4, '\n'
#       '     5        ', freq5, '\n'
#       '     6        ', freq6, '\n'
#       '   Total      ', launch)
# # ***********************************************************
# # Ex4
# from ModuleExercices import fibonacci
#
# print('Inform a Fibonacci term: ')
# fibo = int(input(''))
# for count in range(1, fibo+1):
#     print(fibonacci(count), end=' ')
# # ***********************************************************
# Ex5
# from ModuleExercices import numberCheck
# from ModuleExercices import numberLimit
#
#
# def menu():
#     option = 1
#     while option != 0:
#         print('Choose an option: \n'
#               '1. Perfect number check\n'
#               '2. All perfect numbers\n'
#               '0. Exit')
#         option = int(input())
#         if option == 1:
#             number = int(input('Inform a number: '))
#             if numberCheck(number):
#                 print('%d it is a perfect number.' % number)
#             else:
#                 print('%d it is not a perfect number.' % number)
#             print('**********************************')
#         elif option == 2:
#             number = int(input('Inform a limit number: '))
#             numberLimit(number)
#             print('\n**********************************')
#         elif option == 0:
#             pass
#         else:
#             continue
#
#
# menu()
# # ***********************************************************
# # Ex6
# val = int(input('Inform number: '))
#
# aux = 1
# num = 1
# while aux <= val:
#     for count in range(1, aux + 1):
#         print(num, end=' ')
#
#     print()
#     num += 1
#     aux += 1
# # ***********************************************************
# # Ex7
#
# val = int(input('Inform number: '))
#
# aux = 1
# while aux <= val:
#     for count in range(1, aux + 1):
#         print(count, end=' ')
#
#     print()
#     aux += 1
# # ***********************************************************
