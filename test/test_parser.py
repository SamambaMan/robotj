from unittest import TestCase

from bs4 import BeautifulSoup

from robotj.crawler.parser import parse_metadados, area_dos_metadados
from robotj.test.processos import processo_judicial_1, processo_judicial_2


class Parser(TestCase):
    def _prepara_html(self, html):
        soup_obj = BeautifulSoup(html)
        return soup_obj.find_all('td')

    def test_parse_metadados_processo_judicial(self):
        metadados = parse_metadados(
            processo_judicial_1,
            '0004999-58.2015.8.19.0036'
        )

        expected = {
            'numero_processo': '0004999-58.2015.8.19.0036',
            'status': 'PROCESSO COM BAIXA',
            'comarca': 'Comarca de Nilópolis',
            'comarca_info_1': ('2ª Vara de Família e da Infância e da'
                               ' Juventude e do Idoso'),
            'comarca_info_2': ('Cartório da 2ª Vara de Família, Inf. e da'
                               ' Juv. e do Idoso'),
            'endereco': 'Getúlio Vargas 571 - 6º andar',
            'bairro': 'Olinda',
            'aviso_ao_advogado': '',
            'cidade': 'Nilópolis',
            'acao': ('Medidas Pertinentes Aos Pais Ou '
                     'Responsável / Seção Cível'),
            'assunto': ('Medidas Pertinentes Aos Pais Ou Responsável'
                        ' / Seção Cível'),
            'classe': ('Perda ou Suspensão ou Restabelecimento do Poder '
                       'Familiar'),
            'autor': 'MINISTÉRIO PÚBLICO DO ESTADO DO RIO DE JANEIRO',
            'requerido': 'DANIELLE MARIA GOMES BARBOSA',
            'advogado': 'TJ000002 - DEFENSOR PÚBLICO'}

        for chave, valor in expected.items():
            with self.subTest():
                self.assertEqual(metadados[chave], valor)
    def test_delimita_linhas_dos_metadados_processo_judicial_1(self):
        inicio, fim = area_dos_metadados(
            self._prepara_html(processo_judicial_1)
        )

        inicio_esperado = 6
        fim_esperado = 37

        self.assertEqual(inicio, inicio_esperado)
        self.assertEqual(fim, fim_esperado)
