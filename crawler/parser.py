import re

from bs4 import BeautifulSoup


def parse_metadados(html, numero_processo):
    soup = BeautifulSoup(html, 'html.parser')
    linhas = soup.find_all('td')
    pares= [
        ('status', 6), ('comarca', 8), ('comarca_info_1', 9),
        ('comarca_info_2', 11), ('endereco', 14), ('bairro', 16),
        ('cidade', 18), ('acao', 21), ('assunto', 24), ('classe', 27),
        ('autor', 30), ('requerido', 32), ('advogado', 35)
    ]

    metadados = {}
    metadados['numero_processo'] = numero_processo

    for chave, indice in pares:
        metadados[chave] = re.sub('\s+', ' ', linhas[indice].get_text()).strip()

    return metadados
