# notas = {'Aluno1': 9,
#          'Aluno2': 10,
#          'Aluno3': 4}
#
# for aluno in notas:
#     print("Nota de ", aluno, ": ", notas[aluno])
#
# print(notas.items())
# print(notas.keys())
# print(notas.values())
# # **************************************************
# notas = {'Aluno1': 9,
#          'Aluno2': 10,
#          'Aluno3': 4}

# print(notas)
# notas.setdefault('Aluno4', 8)
# print(notas)
# # **************************************************
# notas = {'Marcelo': 9,
#          'Rafael': 10,
#          'Eliane': 4}
#
# nome = input('Informe nome do aluno: ')
# if notas.get(nome):
#     print('Aluno existente.')
#     print(notas)
# else:
#     nota = int(input('Informe nota do aluno: '))
#     notas[nome] = nota
#     print(notas)
# # **************************************************
# notas = {'Aluno1': 9,
#          'Aluno2': 10,
#          'Aluno3': 4}
#
# nome = input("Aluno a mudar a nota: ")
# nota = float(input("Nova nota     : "))
#
# if nome in notas.keys():
#     notas[nome] = nota
# else:
#     print("Não existe esse aluno")
# print(notas)
# # **************************************************
