# nome = input('Nome: ')
# idade = int(input('Idade: '))
#
# cadastro = [nome, idade]
#
# print(cadastro)
# print(cadastro[0])
# print(cadastro[1])
# # **************************************
# lista = []
#
# while True:
#     print('1. Número\n'
#           '2. Mostrar lista\n'
#           '3. Tamanho\n'
#           '4. Alterar nome')
#     menu = int(input())
#
#     if menu == 1:
#         lista.append(int(input('Número: ')))
#     elif menu == 2:
#         print(lista)
#     elif menu == 3:
#         print('Tamanho: ', len(lista))
#     elif menu == 4:
#         end = int(input('Endereço que deseja alterar: '))
#         if end < len(lista):
#             lista[end] = int(input("Novo número: "))
#         else:
#             print('Endereço inválido.')
#     else:
#         continue
# # **************************************
# semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
#
# if 'Sexta' in semana:
#     print("Sim, ", 'Sexta', " está na lista")
# else:
#     print("Não está")
#
# if 'Semana' not in semana:
#     print('Semana não está na lista')
# else:
#     print("Semana está na lista")
# # **************************************
# matriz = [[0 for i in range(4)] for j in range(4)]
# count = 0
#
# for linha in range(4):
#     for coluna in range(4):
#         matriz[linha][coluna] = count
#         count += 1
#
# for linha in range(4):
#     for coluna in range(4):
#         print("%4d" % matriz[linha][coluna], end='')
#     print()
# # **************************************