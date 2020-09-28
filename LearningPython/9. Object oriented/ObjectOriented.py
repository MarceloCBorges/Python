# class Registro:
#     idade = 0
#
#     def __init__(self):
#         self.nome = input('Informe nome: ')
#
#     def exibe(self):
#         return f'Cadastro: \n' \
#                f'Nome: {self.nome}\n' \
#                f'Idade: {self.idade}'
#
#     def age(self):
#         self.idade = int(input('Informe idade: '))
#
#     def name(self, nome):
#         self.nome = nome
#
#
# def troca():
#     print('Qual dado gostaria de trocar?')
#     print('1. Nome\n'
#           '2. Idade')
#
#     option = int(input())
#
#     if option == 1:
#         nome = input('Informe nome: ')
#         cadastro.name(nome)
#
#     elif option == 2:
#         cadastro.age()
#
#
# cadastro = Registro()
# print(cadastro.exibe())
# print('---------------')
#
# print('Gostaria de alterar algum dado?')
# print('1. Sim\n'
#       '2. Não')
# option = int(input())
#
# if option == 1:
#     troca()
# elif option == 2:
#     status = False
#
# print(cadastro.exibe())
# # ********************************************************

# class Funcionario:
#     def __init__(self, nome):
#         self.__nome = nome
#
#     def retornaNome(self):
#         return self.__nome
#
#
# class Empresa:
#     func = []
#
#     def __init__(self):
#         print("Empresa em funcionamento")
#
#         while True:
#             print("1. Contratar")
#             print("2. Exibir lista de funcionarios")
#             option = int(input())
#
#             if option == 1:
#                 self.contratar()
#             elif option == 2:
#                 self.exibir()
#             else:
#                 print("Opção invalida")
#
#     def contratar(self):
#         nome = input("Nome: ")
#         self.func.append(Funcionario(nome))
#
#     def exibir(self):
#         for funcionario in self.func:
#             print(funcionario.retornaNome())
#
#
# Empresa()
# # ********************************************************
# class Veiculo:
#     def __init__(self, tipo, modelo, km):
#         self.tipo = tipo
#         self.modelo = modelo
#         self.km = km
#
#
# class Carro(Veiculo):
#     def __init__(self, tipo, modelo, km, portas):
#         Veiculo.__init__(self, tipo, modelo, km)
#         self.portas = portas
#
#     def exibe(self):
#         print(self.tipo, "modelo", self.modelo, "com", self.km,
#               "km rodados e", self.portas, "portas.")
#
#
# palio = Carro("Carro", "Palio", "10000", 2)
# palio.exibe()
