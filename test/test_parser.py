from unittest import TestCase, main

from crawler.parser import parse_metadata
from test.fixtures import judicial_process_one


class TestParser(TestCase):
    def test_parse_judicil_process_metadata(self):
        metadata = parse_metadata(
            judicial_process_one,
            '0004999-58.2015.8.19.0036'
        )

        expected = {'numero_processo': '0004999-58.2015.8.19.0036',
                    'status': 'PROCESSO COM BAIXA',
                    'comarca': 'Comarca de Nilópolis',
                    'comarca_info_1': '2ª Vara de Família e da Infância e da Juventude e do Idoso',
                    'comarca_info_2': 'Cartório da 2ª Vara de Família, Inf. e da Juv. e do Idoso',
                    'endereco': 'Getúlio Vargas 571 - 6º andar',
                    'bairro': 'Olinda',
                    'cidade': 'Nilópolis',
                    'acao': 'Medidas Pertinentes Aos Pais Ou Responsável / Seção Cível',
                    'assunto': 'Medidas Pertinentes Aos Pais Ou Responsável / Seção Cível',
                    'classe': 'Perda ou Suspensão ou Restabelecimento do Poder Familiar',
                    'autor': 'MINISTÉRIO PÚBLICO DO ESTADO DO RIO DE JANEIRO',
                    'requerido': 'DANIELLE MARIA GOMES BARBOSA',
                    'advogado': 'TJ000002 - DEFENSOR PÚBLICO'}

        for key, value in expected.items():
            with self.subTest():
                self.assertEqual(metadata[key], value)
