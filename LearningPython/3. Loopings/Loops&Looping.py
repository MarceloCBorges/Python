# val = int(input('Informe valor para impressão em ordem decrescente: '))
#
# while val != 0:
#     print(val)
#     val -= 1
#
# print('FIM')
# ------------------------------------------------
# num = float(input('Informe um número: '))
#
# while num != 0:
#     num = float(input('Informe outro número: '))
#
# print('FIM')
# ------------------------------------------------
# for num in [1, 2, 3, 4, 5]:
#     print(num)
# ------------------------------------------------
# for num in ["Bom", "dia", 'estudante', "!!"]:
#     print(num)
# ------------------------------------------------
# for val in range(5):
#     print(val+1)
# ------------------------------------------------
# for val in range(1, 6):
#     print(val)
# ------------------------------------------------
# for val in range(2, 101, 2):
#     print(val)
# ------------------------------------------------
# valor_inicial = int(input("Valor inicial: "))
# valor_final= int(input("Valor final: "))
#
# valor_final = valor_final + 1
#
# for var in range(valor_inicial, valor_final):
#     print(var)
# ------------------------------------------------
# # Crie um programa em Python que pede um número inteiro ao usuário e calcule seu fatorial.
#
# num = int(input("Inform factorial value: "))
# result = 1
#
# while num != 0:
#     result *= num
#     num -= 1
#
# print(result)
# ------------------------------------------------
# hora = 0
# minuto = 0
# segundo = 0
#
# for minuto in range(60):
#     for segundo in range(60):
#         print(hora, ':', minuto, ':', segundo)
#
# hora += 1
# print(hora, ':', minuto, ':', segundo)
# ------------------------------------------------
# linCol = int(input('Número da Matriz desejada [ZxZ]: '))
# lCount = 0
# cCount = 0
#
# for lCount in range(linCol):
#     for cCount in range(linCol):
#         print('x ', end='')
#     print()
# ------------------------------------------------
# total = 0
#
# for count in range(1000):
#     count += 1
#     if count % 3 == 0:
#         continue
#     total += count
#
# print(total)
# ------------------------------------------------
