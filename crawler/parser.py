import re

from bs4 import BeautifulSoup


def parse_metadados(html, numero_processo):
    soup = BeautifulSoup(html, 'html.parser')
    linhas = soup.find_all('td')
    metadados = {
        'status': '',
        'comarca': '',
        'comarca_info_1': '',
        'comarca_info_2': '',
        'endereco': '',
        'bairro': '',
        'cidade': '',
        'acao': '',
        'assunto': '',
        'classe': '',
        'aviso_ao_advogado': '',
        'autor': '',
        'requerido': '',
        'advogado': ''
    }
    pares = [
        ('status', 6), ('comarca', 8), ('comarca_info_1', 9),
        ('comarca_info_2', 11), ('endereco', 14), ('bairro', 16),
        ('cidade', 18), ('acao', 21), ('assunto', 24), ('classe', 27),
        ('autor', 30), ('requerido', 32), ('advogado', 35)
    ]

    metadados['numero_processo'] = numero_processo

    for chave, indice in pares:
        metadados[chave] = re.sub(
            '\s+', ' ', linhas[indice].get_text()).strip()

    return metadados


def area_dos_metadados(linhas_de_dados):
    # Aparentemente esse valor e fixo
    inicio = 6
    for indice, linha in enumerate(linhas_de_dados):
        if 'Tipo do Movimento:' in linha.get_text():
            fim = indice - 1
            break

    return inicio, fim


def limpa_conteudo(conteudo_sujo):
    return re.sub('\s+', ' ', conteudo_sujo).strip()
