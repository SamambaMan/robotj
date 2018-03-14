from slugify import slugify

from robotj.crawler.utils import limpa_conteudo


def parse_metadados(linhas_de_dados, numero_processo, inicio_metadados,
                    fim_metadados):
    metadados = {
        'status': [''],
        'endereco': [''],
        'bairro': [''],
        'cidade': [''],
        'acao': [''],
        'assunto': [''],
        'classe': [''],
        'aviso_ao_advogado': [''],
        'autor': [''],
        'requerido': [''],
        'requerente': [''],
        'advogado-s': ['']
    }

    # Delimita o processo na regiao dos metadados
    linhas_com_metadados = linhas_de_dados[inicio_metadados:fim_metadados]

    metadados['numero_processo'] = numero_processo
    metadados['status'] = limpa_conteudo(
        linhas_com_metadados[0].find_all('td')[0].get_text()
    )

    del linhas_com_metadados[:2]
    dados_comarca = []
    for tr in list(linhas_com_metadados):
        linhas_com_metadados.pop(0)
        if len(tr.find_all('td')) == 1:
            break
        dados_comarca += [tr]

    # TODO: refatorar
    textos = []
    for tr in dados_comarca:
        for td in tr.find_all('td'):
            textos += list(
                filter(None, [limpa_conteudo(td.get_text()) if td else ''])
            )

    metadados['comarca'] = textos

    for tr in list(linhas_com_metadados):
        linhas_com_metadados.pop(0)
        linha = []
        tds = tr.find_all('td')
        for td in tds:
            linha += list(
                filter(None, [limpa_conteudo(td.get_text()) if td else ''])
            )

            if linha:
                metadados[slugify(linha[0])] = linha[1:]

    return metadados


def area_dos_metadados(linhas_de_dados):
    # Aparentemente esse valor e fixo
    inicio = 6
    for indice, linha in enumerate(linhas_de_dados):
        if 'Tipo do Movimento:' in linha.get_text():
            fim = indice - 1
            break

    return inicio, fim
