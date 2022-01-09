from google.oauth2 import service_account
import pandas_gbq
import os
import time

path = os.getcwd()

credentials = service_account.Credentials.from_service_account_file(
    f'{path}/main/scraping-python-google-play-scraper/database/credentials/scrap-sauter-b84203485905.json',
)


def excluir_tabelas():
    try:
        sql = """
        DROP TABLE scrap-sauter.Tables.positivas ;

        DROP TABLE scrap-sauter.Tables.neutras ;

        DROP TABLE scrap-sauter.Tables.negativas
        """

        df = pandas_gbq.read_gbq(sql, project_id="scrap-sauter", credentials=credentials)

    except:
        print('_____________ Acionando a Inserção das Tabelas no Banco de Dados _____________')
        time.sleep(3)
        import insert_tables


excluir_tabelas()
