import re

from bs4 import BeautifulSoup


def parse_metadata(html, doc_number):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('td')
    pairs = [
        ('status', 6), ('comarca', 8), ('comarca_info_1', 9),
        ('comarca_info_2', 11), ('endereco', 14), ('bairro', 16),
        ('cidade', 18), ('acao', 21), ('assunto', 24), ('classe', 27),
        ('autor', 30), ('requerido', 32), ('advogado', 35)
    ]

    metadata = {}
    metadata['numero_processo'] = doc_number

    for key, row in pairs:
        metadata[key] = re.sub('\s+', ' ', rows[row].get_text()).strip()

    return metadata
