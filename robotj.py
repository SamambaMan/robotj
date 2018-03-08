from sqlalchemy import create_engine
from lyraextrator.settings import DS_EXADATA_CONN_CSTR, engine
from lyraextrator.datasources.mcpr import obter_documentos_externos


def main():
    engine['connection'] = create_engine(
        DS_EXADATA_CONN_CSTR,
        convert_unicode=False,
        pool_recycle=10,
        pool_size=50,
        echo=True
    )

    linhas = obter_documentos_externos()
    for linha in linhas:
        print(linha['docu_nr_externo'])

if  __name__ =='__main__':main()
