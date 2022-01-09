import pandas as pd
import time

def inserir_dados():
    positiva = pd.read_csv('../df_positiva.csv', sep='|')
    positiva.to_gbq(destination_table='Tables.positivas',
                    project_id='scrap-sauter',
                    if_exists='replace')

    neutra = pd.read_csv('../df_neutra.csv', sep='|')
    neutra.to_gbq(destination_table='Tables.neutras',
                  project_id='scrap-sauter',
                  if_exists='replace')

    negativa = pd.read_csv('../df_negativa.csv', sep='|')
    negativa.to_gbq(destination_table='Tables.negativas',
                    project_id='scrap-sauter',
                    if_exists='replace')


inserir_dados()

time.sleep(5)

def limpar_diretorio():

    print('_____________ Acionando a Limpeza da Raiz _____________')
    import limpardf


limpar_diretorio()
