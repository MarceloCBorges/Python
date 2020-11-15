import re

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

valor = 0
periodo = ''
circuit_id = ''


def tim():
    global valor, circuit_id, periodo
    for page_layout in extract_pages("TIM.PDF"):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                if re.search(r"^TOTAL:", element.get_text()):
                    # busca pelo valor total
                    index = re.search(r'\d', element.get_text()).start()
                    valor = element.get_text()[index:]

                if re.search(r'^ITH_', element.get_text()):
                    index = re.search(r'\s', element.get_text()).start()
                    circuit_id = element.get_text()[:index]

                if re.findall(r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9] a', element.get_text()):
                    index = re.search(r'[0-9][0-9]/', element.get_text()).start()
                    periodo = element.get_text()[index-1:].strip()



tim()
print(f'Circuit_ID:{circuit_id}')
print(f'Valor:{valor}')
print(f'Mes referencia:{periodo}')
