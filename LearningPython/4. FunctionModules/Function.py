# def mensagem():
#     print("Olá, mundo")
#
#
# while 1:
#     mensagem()
# # **************************************************

# def soma():
#     x = float(input("Primeiro numero: "))
#     y = float(input("Segundo numero: "))
#     soma = x + y
#     print("Soma: ", soma)
#
#
# continuar = 1
#
# while continuar:
#     if continuar:
#         soma()
#     continuar = int(input("Digite 0 se desejar encerrar ou qualquer outro numero para continuar: "))
# # **************************************************
# def soma():
#     a = float(input("Primeiro numero: "))
#     b = float(input("Segundo numero: "))
#     print('Resultado: ', a + b)
#     print('*********************')
#
#
# def subtracao():
#     a = float(input("Primeiro numero: "))
#     b = float(input("Segundo numero: "))
#     print('Resultado: ', a - b)
#     print('*********************')
#
#
# def multiplicacao():
#     a = float(input("Primeiro numero: "))
#     b = float(input("Segundo numero: "))
#     print('Resultado: ', a * b)
#     print('*********************')
#
#
# def divisao():
#     a = float(input("Primeiro numero: "))
#     b = float(input("Segundo numero: "))
#     print('Resultado: ', a / b)
#     print('*********************')
#
#
# menu = 1
#
# while menu != 0:
#     print('1. Soma\n'
#           '2. Subtracao\n'
#           '3. Multiplicação\n'
#           '4. Divisao\n'
#           '0. Sair')
#     menu = int(input())
#
#     if menu == 1:
#         soma()
#     elif menu == 2:
#         subtracao()
#     elif menu == 3:
#         multiplicacao()
#     elif menu == 4:
#         divisao()
#     elif menu > 4:
#         print('Função inválida.')
# # **************************************************
# # com passagem de argumentos
#
# def soma(a, b):
#     print('Resultado: ', a + b)
#     print('*********************')
#
#
# def subtracao(a, b):
#     print('Resultado: ', a - b)
#     print('*********************')
#
#
# def multiplicacao(a, b):
#     print('Resultado: ', a * b)
#     print('*********************')
#
#
# def divisao(a, b):
#     print('Resultado: ', a / b)
#     print('*********************')
#
#
# menu = 1
#
# while menu != 0:
#     a = float(input("Primeiro numero: "))
#     b = float(input("Segundo numero: "))
#     print('1. Soma\n'
#           '2. Subtracao\n'
#           '3. Multiplicação\n'
#           '4. Divisao\n'
#           '0. Sair')
#     menu = int(input('Operação: '))
#
#     if menu == 1:
#         soma()
#     elif menu == 2:
#         subtracao()
#     elif menu == 3:
#         multiplicacao()
#     elif menu == 4:
#         divisao()
#     elif menu > 4:
#         print('Função inválida.')
# # **************************************************
# def somatorio(x):
#     if x == 1:
#         return 1
#     else:
#         return x + somatorio(x - 1)
#
#
# while True:
#     x = int(input("Somatorio de 1 até: "))
#     print("Soma: ", somatorio(x))
# # **************************************************
# def soma(x, y):
#     result = x + y
#     return result
#
#
# a = int(input("Primeiro numero: "))
# b = int(input("Segundo numero : "))
# res = soma(a, b)
# print("Soma: ", res)
# # **************************************************
