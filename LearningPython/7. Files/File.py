# # Ao chegar no final do arquivo, é criado um 'flag' automático, informando que arquivo terminou.
# arquivo = open('../7. Files/File/teste.txt')
# print(arquivo.read())
# linha = arquivo.readlines()
# print('--> Número de linhas: ', len(linha))
# print('**************')
#
# arquivo = open('../7. Files/File/teste.txt')
# linha = arquivo.readlines()
# print(linha)
# print('**************')
#
# arquivo = open('../7. Files/File/teste.txt')
# linha = arquivo.readline()
# print(linha)
# linha = arquivo.readline()
# print(linha)
# print('**************')
#
# arquivo = open('../7. Files/File/teste.txt', 'w')
# arquivo.write('linha 1')
# arquivo.close()
# print('**************')
#
# arquivo = open('../7. Files/File/teste.txt', 'a')
# arquivo.write('\nlinha 2')
# arquivo.close()
#
# arquivo = open('../7. Files/File/teste.txt', 'r')
# linha = arquivo.readlines()
#
# for line in linha:
#     line = line.rstrip('\n')
#     print(line)
# print('********************************************************')
# arquivo = open('../7. Files/File/linguagem.txt', 'r')
# num = int(input("Numero de linguagens: "))
# count = 0
#
# for linha in arquivo:
#     if count < num:
#         print(count + 1, ':', linha.rstrip('\n'))
#         count = count + 1
#     else:
#         break
#
# arquivo.close()
# print('********************************************************')
# import os
#
# path = os.getcwd()
# dirs = os.listdir(path)
#
# for file in dirs:
#     print(file)
# # print('********************************************************')

