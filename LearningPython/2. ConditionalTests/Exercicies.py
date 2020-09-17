# print('EX1')
# letter = input('Type a letter: ')
#
# # .lower() -> converte variável para minúsculo
# # .upper() -> converte variável para maiúsculo
#
# if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or \
#         letter.lower() == 'u':
#     print('The leater is a vowel.')
# else:
#     print('The letter is a consonant.')
# ------------------------------------------------------------------------------------
# print('EX2')
#
# grade1 = float(input('Inform student`s first grade: '))
# grade2 = float(input("Inform student`s second grade: "))
#
# average = (grade1+grade2)/2
#
# if average < 7:
#     print('Failed student')
# else:
#     if average == 10:
#         print('Approved wih perfection')
#     else:
#         print('Approved student')
# ------------------------------------------------------------------------------------
# print('EX3')
#
# value1 = int(input('Inform first number: '))
# value2 = int(input('Inform second number: '))
# value3 = int(input('Inform third number: '))
#
# highest = value1
# lowest = value1
#
# if value2 > highest:
#     highest = value2
# if value3 > highest:
#     highest = value3
# if lowest > value2:
#     lowest = value2
# if lowest > value3:
#     lowest = value3
#
# print("Highest number is: %d" % highest)
# print('Lowest number is: %d' % lowest)
# ------------------------------------------------------------------------------------
# print("EX4")
#
# number = int(input('Type a number: '))
#
# if number % 2 == 0:
#     print('Number %d is a even number.' % number)
# else:
#     print('Number %d is a odd number.' % number)
# ------------------------------------------------------------------------------------
# print("EX5")
#
# number1 = int(input("Inform first number: "))
# number2 = int(input('Inform second number: '))
#
# temp = number1
# number1 = number2
# number2 = temp
#
# print('Now your first number is: ', number1)
# print('Now your second number is: ', number2)
# ------------------------------------------------------------------------------------
# print('EX6')
#
# salary = float(input('Inform the salary: '))
#
# if salary <= 280.00:
#     percentage = 0.2
# elif 280.00 < salary <= 700.00:
#     percentage = 0.15
# elif 780.00 < salary <= 1500.00:
#     percentage = 0.1
# else:
#     percentage = 0.05
#
# print('Old salary: $', salary)
# print(f"Salary increase: {(percentage*100):.0f}%")
# print('Amount: $', salary*percentage)
# print('New salary: $', salary+(salary*percentage))
# ------------------------------------------------------------------------------------
# print('EX7')
#
# price_hour = float(input('Inform hour price: '))
# work_hour = float(input('Inform hours worked: '))
#
# gross = work_hour * price_hour
# ir = gross*.05
# inss = gross*.1
# fgts = gross*.11
#
# print('Gross salary: $', gross)
# print('Income taxes: $-', ir)
# print('INSS: $-', inss)
# print('FGTS: $', fgts)
# print('Total discount: $-', ir+inss)
# print('Net salary: ', gross-(ir+inss))
# ------------------------------------------------------------------------------------
# print('EX8')
#
# side1 = float(input('Inform triangle side 1: '))
# side2 = float(input('Inform triangle side 2: '))
# side3 = float(input('Inform triangle side 3: '))
#
# if (side1 + side2) < side3 or (side2 + side3) < side1 or (side1 + side3) < side2:
#     print('It is not a triangle.')
# elif side1 == side2 and side1 == side3:
#     print('Equilateral Triangle.')
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print('Isosceles triangle.')
# else:
#     print('Scalene triangle.')
# ------------------------------------------------------------------------------------
# import math
#
# print('EX9')
#
# a = int(input("'A' coefficient: "))
#
# if a == 0:
#     print("It is not a quadratic function.")
# else:
#     b = float(input("'B' coefficient: "))
#     c = float(input("'C' coefficient: "))
#
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print('Function does not have real roots.')
#     elif delta == 0:
#         print(f'Only one possible root: {(-b / (2 * a)):.2f}')
#     else:
#         print(f'Root 1: {((-b + math.sqrt(delta)) / (2 * a)):.2f}')
#         print(f'Root 2: {((-b - math.sqrt(delta)) / (2 * a)):.2f}')
# ------------------------------------------------------------------------------------
# print('EX10')
#
# value = float(input('Inform a number lower than a thousand: '))
#
# unit = value % 10
# value = ((value - unit) / 10)
# dozen = value % 10
# value = value - dozen
# hundred = value / 10
#
# print('%d hundred' % hundred)
# print('%d dozen' % dozen)
# print('%d unit' % unit)
# ------------------------------------------------------------------------------------
# print('EX11')
# value = int(input('Inform a value to withdraw: '))
#
# hundred = int(value / 100)
# value = value - (hundred * 100)
#
# fifty = int(value / 50)
# value = value - (fifty * 50)
#
# ten = int(value / 10)
# value = value - (ten * 10)
#
# five = int(value / 5)
# value = value - (five * 5)
#
# unit = value
#
# if not hundred == 0:
#     print('$100: ', hundred)
# if not fifty == 0:
#     print('$50: ', fifty)
# if not ten == 0:
#     print('$10: ', ten)
# if not five == 0:
#     print('$5: ', five)
# if not unit == 0:
#     print('$1: ', unit)
# ------------------------------------------------------------------------------------
# print('EX12')
#
# print('Type of fuel: \n'
#       '1. Gasoline\n'
#       '2. Alcohol')
#
# fuel = int(input('Type: '))
#
# if not fuel == 1 or fuel == 2:
#     print("Fuel not found. Try another type.")
# else:
#     liter = float(input('Quantity: '))
#     if fuel == 1:
#         if liter > 20:
#             price = 2.50
#             discount = (2.50 * liter) * .05
#             final_price = (price * liter) - discount
#             price_liter = final_price / liter
#             print('Fuel type: Gasoline')
#
#         else:
#             price = 2.50
#             discount = (2.50 * liter) * .03
#             final_price = (price * liter) - discount
#             price_liter = final_price / liter
#             print('Fuel type: Gasoline')
#     else:
#         if liter > 20:
#             price = 1.90
#             discount = (2.50 * liter) * .06
#             final_price = (price * liter) - discount
#             price_liter = final_price / liter
#             print('Fuel type: Alcohol')
#         else:
#             price = 1.90
#             discount = (2.50 * liter) * .04
#             final_price = (price * liter) - discount
#             price_liter = final_price / liter
#             print('Fuel type: Alcohol')
#
#     print(f'Fuel price: ${price:.2f}')
#     print(f'Discount: ${discount:.2f}')
#     print(f'Price per liter: ${price_liter:.2f}')
#     print(f'To pay: ${final_price:.2f}')
#     ------------------------------------------------------------------------------------
# print('EX13')
#
# print('Product: \n'
#       '1. Filet\n'
#       '2. Alcatra\n'
#       '3. Picanha')
#
# menu = int(input('Choose a product: '))
#
# if not menu == 1 or menu == 2 or menu == 3:
#     print('Product not found. Choose another one.')
# else:
#     if menu == 1:
#         product = 'Filet'
#         quantity = float(input('Serving Size[KG]: '))
#         if quantity < 5:
#             price = 4.90
#             final_price = price * quantity
#         else:
#             price = 5.80
#             final_price = price * quantity
#         print('\n')
#     elif menu == 2:
#         product = 'Alcatra'
#         quantity = float(input('Serving Size[KG]: '))
#         if quantity < 5:
#             price = 5.90
#             final_price = price * quantity
#         else:
#             price = 6.80
#             final_price = price * quantity
#         print('\n')
#     else:
#         product = 'Picanha'
#         quantity = float(input('Serving Size[KG]: '))
#         if quantity < 5:
#             price = 6.90
#             final_price = price * quantity
#         else:
#             price = 7.80
#             final_price = price * quantity
#         print('\n')
#
#     print('Product: ', product)
#     print(f'KG: ${price:.2f}')
#     print(f'Quantity: {quantity:.2f} [KG]')
#     print(f'Total: ${final_price:.2f}')
#
#     print('\nPayment: \n'
#           '1. Cash\n'
#           '2. Credit card')
#     payment = int(input('Payment method: '))
#     print('\n')
#     if not payment == 1 or payment == 2:
#         print('Invalid payment method.')
#     else:
#         if payment == 1:
#             final_price = final_price - (final_price * .05)
#             print('Product: ', product)
#             print(f'KG: ${price:.2f}')
#             print(f'Quantity: {quantity:.2f}[KG]')
#             print(f'Discount: ${(final_price * .05):.2f}')
#             print(f'Total: ${final_price:.2f}')
#         else:
#             print('Product: ', product)
#             print(f'KG: ${price:.2f}')
#             print(f'Quantity: {quantity:.2f}[KG]')
#             print(f'Total: ${final_price:.2f}')
# ------------------------------------------------------------------------------------