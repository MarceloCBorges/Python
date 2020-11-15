from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

print('Arquivo')
for page_layout in extract_pages("Embratel.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            print(repr(element.get_text()))
            # print(element.get_text())
