import re

import numpy as np
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

import globalVar as gv

id_list = np.array([])
valor_list = np.array([])
periodo_list = np.array([])


def list_to_matriz():
    matriz = np.concatenate((id_list, valor_list, periodo_list))
    print('Matriz-----')
    print(matriz)


def find_values():
    global id_list, periodo_list, valor_list
    for page_layout in extract_pages("Embratel.pdf"):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                if re.search(r'Origem:', element.get_text()):
                    index_start = re.search(r'\s', element.get_text()).start()
                    index_end = re.search(r'\n', element.get_text()).start()
                    gv.circuit_id = element.get_text()[index_start + 1:index_end]
                    index_start = re.search(r'[0-9][0-9]/', element.get_text()).start()
                    index_end = re.search(r'/[0-9][0-9]\n', element.get_text()).start()
                    gv.periodo = element.get_text()[index_start:index_end + 3]
                    id_list = np.append(id_list, gv.circuit_id)
                    periodo_list = np.append(periodo_list, gv.periodo)

                if re.search(r'Subtotal:', element.get_text()):
                    index_start = re.search(r'\d', element.get_text()).start()
                    gv.valor = element.get_text()[index_start - 1:].strip()
                    valor_list = np.append(valor_list, gv.valor)

    list_to_matriz()


find_values()
