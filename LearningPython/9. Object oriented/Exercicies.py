# # Ex1
# import random
#
#
# class HeadsTail:
#     def __init__(self):
#         self.coin = 'Heads'
#
#     def launch(self):
#
#         if random.randint(0, 1) == 0:
#             self.coin = 'Heads'
#         else:
#             self.coin = "Tails"
#
#         return self.coin
#
#
# class Dice:
#     def __init__(self):
#         self.dice = 0
#
#     def launch(self):
#         self.dice = random.randint(1, 6)
#         return self.dice
#
#
# def menu():
#     option = 1
#
#     coin = HeadsTail()
#     dice = Dice()
#
#     while option != 0:
#         print('1. Heads or Tails\n'
#               '2. Dice\n'
#               '0. exit')
#
#         option = int(input())
#
#         if option == 1:
#             print('-----------------')
#             print('Head Tails flip')
#             print('--> ', coin.launch())
#             print('-----------------')
#         elif option == 2:
#             print('-----------------')
#             print('Dice launch')
#             print('--> ', dice.launch())
#             print('-----------------')
#         elif option == 0:
#             pass
#         else:
#             print('No valid option.')
#
#
# menu()
# #  ****************************************
# # Ex2
# class Account:
#
#     def __init__(self):
#         self.amount = 0
#
#     def amount(self):
#         return self.amount
#
#
# class PA(Account):  # Physical account
#     def __init__(self):
#         Account.__init__(self)
#
#     def deposit(self, value):
#         self.amount += value
#
#     def withdraw(self, value):
#         self.amount -= value
#
#
# class JA(Account):  # Juridical account
#     def __init__(self):
#         Account.__init__(self)
#
#     def deposit(self, amount):
#         self.amount += amount
#
#     def withdraw(self, amount):
#         self.amount -= amount
#
#
# def money(acc):
#     while True:
#         print('1. Deposit\n'
#               '2. Withdraw\n'
#               '3. Total amount')
#         opt = int(input('Menu: '))
#
#         if opt == 1:
#             amount = float(input('Value to deposit: '))
#             if amount >= 0:
#                 acc.deposit(amount)
#                 print('Deposit accomplished.')
#                 print('********************')
#             else:
#                 print('Deposito cannot be lower than 0.')
#         elif opt == 2:
#             amount = float(input('Value to withdraw: '))
#             if amount > acc.amount:
#                 print('You don`t have this amount to withdraw.')
#                 print('Amount: ', acc.amount)
#             else:
#                 acc.withdraw(amount)
#                 print('New amount: ', acc.amount)
#                 print('********************')
#                 break
#         elif opt == 3:
#             print('Total: ', acc.amount)
#         else:
#             print('Invalid menu option.')
#
#
# while True:
#     print("1. Conta física\n"
#           "2. Conta Jurídica\n")
#     opt = int(input('Menu: '))
#
#     if opt == 1:
#         account = PA()
#         print('********************')
#         print('Physical account')
#         money(account)
#         print('********************')
#     elif opt == 2:
#         account = JA()
#         print('********************')
#         print('Physical account')
#         money(account)
#         print('********************')
#     else:
#         print('Invalid menu option')
