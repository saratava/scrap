import os
import time


def etc():
    print('_____________ Iniciando Limpeza  _____________')
    path = os.getcwd()
    diretorios = os.listdir(path)
    print()
    time.sleep(3)
    try:
        for arquivo in diretorios:
            if arquivo == "df_neutra.csv" or arquivo == "df_positiva.csv" or arquivo == "df_negativa.csv" or arquivo == "Report_Negativas.html" or arquivo == "Report_Positivas.html" or arquivo == "Report_Neutras.html":
                os.remove(arquivo)
                print(f'Arquivo = {arquivo} apagado')
    except:
        print('Algo aconteceu e a limpeza não foi feita')

    print('_____________ Limpeza Concluída _____________\n')
    print(
        '##################  Programa executado com êxito ###################\n# Ações Executadas:                                                #\n# 1- App Scraping de Reviews do app Alexa na Google Play Store     #\n# 2- Limpeza e Filtragem de Dados                                  #\n# 3- Geração de 3 arquivos csv filtradas pela avaliação            #\n#    dos usuários                                                  #\n# 4- Geração de Reports de análise dos dados coletados             #\n# 5- Gravação de informações no banco de dados                     #\n# 6- Limpeza do diretório de origem dos arquivos CSV               #\n#                                                                  #\n####################################################################\n')



etc()

#  Editar a mensagem de conclusão !!!!!!!

# import request_database
# print(request_database.database)

# /home/sarat/Área de Trabalho/scraping-python-google-play-scraper/sheets

##################  Programa executado com êxito ###################\n
# Ações Executadas:                                                #\n
# 1- App Scraping de Reviews do app Alexa na Google Play Store     #\n
# 2- Limpeza e Filtragem de Dados                                  #\n
# 3- Geração de 3 arquivos csv's filtradas pela avaliação          #\n
# dos usuários                                                     #\n
# 4- Geração de Reports de análise dos dados coletados             #\n
# 5- Gravação de informações no banco de dados                     #\n
# 6- Limpeza do diretório de origem dos arquivos CSV               #\n
#                                                                  #\n
####################################################################\n
