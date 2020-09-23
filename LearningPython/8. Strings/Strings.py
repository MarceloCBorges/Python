# texto = "Leitura de texto"
#
# for caractere in texto:
#     print(caractere)
#
# num = 0
# for count in texto:
#     print(texto[num], end=' ')
#     num += 1
#
# # *********************************************
# texto = input("Digite uma string: ")
#
# if texto.isalpha():
#     print("Tudo tudo letra")
#     if texto.isupper():
#         print('String maiúscula.')
#     elif texto.islower():
#         print('String minúscula.')
#     else:
#         print('String mista.')
# elif texto.isdecimal():
#     print("Tudo numero")
# elif texto.isalnum():
#     print("Numeros e letras")
# elif texto.isspace():
#     print("Composto so de espaço, e/ou tabulação e/ou quebra de linha")
# else:
#     print("Vazia ou caractere especial")
# # *********************************************
# lista = ['a', 'b', 'c', 'd']
# print(lista)
# print(', '.join(lista))
# print(' -> '.join(lista))
# texto = 'Sempre estudar um pouco por-dia'
# print(texto.split())
# print(texto.split('-'))
# # *********************************************
# texto = 'Trocar trexo escrito erado.'
# print('Sem correção-> ', texto)
# texto = texto.replace('trexo', 'trecho')
# texto = texto.replace('erado', 'errado')
# print('Com correção-> ', texto)
# # *********************************************
# import re
#
# while True:
#     texto = input("Numero no formato 'xxxx-yyyy': ")
#
#     minhaRegex = re.compile(r'\d{4}-\d{4}')
#     resultado = minhaRegex.search(texto)
#     resultado2 = re.findall(r'\d{4}', texto)
#
#     print(resultado.group())
#     print(resultado2)
# # *********************************************
# import re
#
# while True:
#     texto = input("Digite sua string: ")
#
#     minhaRegex = re.compile(r'(\d{2}) (\d{4})-(\d{4})')
#     resultado = minhaRegex.search(texto)
#
#     print("Numero detectado:", resultado.group())
#     print("DDD desse numero:", resultado.group(1))
# # *********************************************
# import re
#
# while True:
#     texto = input("Digite sua string: ")
#
#     minhaRegex = re.findall(r'\d{2} \d{4}-\d{4}|\d{2} \d{8}|\d{8}', texto)
#     print("Telefone: ", minhaRegex)
# # *********************************************
# import re
#
# while True:
#     texto = input("Digite sua string: ")
#
#     minhaRegex = re.compile(r'\d{2}( )*\d{4}(-)?\d{4}')
#     resultado = minhaRegex.search(texto)
#     print(resultado.group())
# # *********************************************
# # Busca por e-mails que contenham letras ou números no início e terminam com '.com'
# import re
#
# while True:
#     texto = input("Digite sua string: ")
#
#     minhaRegex = re.findall(r'^\w+\.\w{3}$', texto)
#     print(minhaRegex)
# # *********************************************
# import re
#
# while True:
#     texto = input("Digite sua string: ")
#
#     minhaRegex = re.findall(r'.ato', texto)
#     print(minhaRegex)
# # *********************************************
# import re
#
# while True:
#     texto = input("Digite sua string: ")
#
#     minhaRegex = re.compile(r'(beba) (agua)')
#     minhaRegex = minhaRegex.sub('\1 (Não) \2 (esquece)', texto)
#
#     print(minhaRegex)
# # *********************************************
# import re
#
# while True:
#     texto = input("Digite sua string: ")
#
#     emailRegex = re.compile(r'''(
#           [a-zA-Z0-9._%+-]+		# nome do usuário
#           @				# arroba
#           [a-zA-Z0-9.-]+    	# domínio
#           (\.[a-zA-Z]{3})   	# ponto seguido de outros caracteres
#           )''', re.VERBOSE)
#
#     print(emailRegex.group())
# # *********************************************
