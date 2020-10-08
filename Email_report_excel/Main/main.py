import getpass  # nome de usuário do windows -> fazer mini tutorial
import os
from datetime import date
from datetime import datetime
from pathlib import Path  # diretórios -> fazer tutorial
from tkinter.filedialog import askopenfilename  # abrir janela para abrir arquivo

import PySimpleGUI as Sg  # biblioteca pysimplegui -> fazer tutorial
import pandas as pd  # biblioteca pandas -> fazer tutorial

# ATUAL: TENTA ABRIR ARQUIVO COM ENDEREÇO, CASO APRESENTE ERRO, ABRE OPCAO PARA ESCOLHER ARQUIVO E CRIA/SALVA NO
# ARQUIVO identificar tipo de arquivo que foi escolhido. caso formato certo (excel) continua programa,
# caso contrário, pede para escolher outro arquivo

# alterar de desktop para documents
user = getpass.getuser()
data_hoje = date.today()
# data_final_projeto = date.today()

caminho = Path("C:/Users/", user, 'Desktop/ProjectDataAddress.txt')

list_status = {}  # projetos e datas para vencimento
list_empty_date = []  # não possui data final de contrato
list_double = []  # projetos que tenham mesmo nome que outros


def new(nome, delay):  # inserção nome lista
    if list_status.get(nome):
        list_double.append(nome)
    else:
        list_status[nome] = delay


def data_vazia(nome):  # caso não contenha data
    list_empty_date.append(nome)


def show():
    string = "Lista chaves: "
    for key in list_status.keys():
        string += key + ' '

    print(string)
    print('lista vazia: ' + str(list_empty_date))


# leitura do arquivo e envio de informações para listas
def file_read(file):
    for line in range(len(file)):  # range de linhas, do início ao fim
        if file.loc[line]['Status'] == "Pendente":  # verifica se status é pendente
            if pd.isna(file.loc[line]["DataFinal"]):  # valida se possui data final informada
                # insere nome do projeto que nao possui data final em uma lista
                data_vazia(file.loc[line]["Nome"])
            else:
                data_final_projeto = datetime.date(file.loc[line]['DataFinal'])  # pega data final do projeto
                data_delay = data_final_projeto - data_hoje  # calculo para diferença de dias
                new(file.loc[line]["Nome"], data_delay.days)


def path_file():
    try:
        arquivo = open(caminho.absolute(), 'r')
        return True, arquivo.read()
    except FileNotFoundError:
        endereco_arquivo = askopenfilename(initialdir="C:/",
                                           filetypes=(
                                               ("All Files", "*.*"), ("Excel File", "*.xlsx"),
                                               ("Excel File", "*.xlsxs")),
                                           title="Choose master file")
        arquivo_nome, extencao = os.path.splitext(endereco_arquivo)  # identifica nome arquivo + extensão
        if extencao == '.xls' or extencao == '.xlsx':  # verifica se arquivo aberto é um arquivo excel
            arquivo = open(caminho.absolute(), 'w')
            arquivo.write(endereco_arquivo)
            arquivo.close()
            return True, endereco_arquivo  # abre arquivo para leitura (pandas)
        else:
            Sg.popup('Error in file extension. File could not be opened.\n'
                     'Choose a excel file (.xls or .xlsx).', title='Error')
            return False


status, endereco = path_file()

if status:
    file = pd.read_excel(endereco)
    file_read(file)

show()

# print(file.columns)  # pega título das colunas
# print(file["Nome"][0])  # busca informação específica de célula Coluna x Linha
# print(file.loc[0])  # pega toda informação da linha de acordo com índex escolhido
