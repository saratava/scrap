import os

def etc():
    print('_____________ Iniciando Limpeza  _____________')
    path = os.getcwd()
    dir = os.listdir(path)
    print(path)
    for file in dir:
        if file == "df_neutra.csv" or file == "df_positiva.csv" or file == "df_negativa.csv" or file == "Report_Negativas.html" or file == "Report_Positivas.html" or file == "Report_Neutras.html":
            os.remove(file)
etc()

print('_____________ Limpeza Concluída _____________\n')

print('##################  Programa executado com êxito ###################\n# Ações Executadas:                                                #\n# 1- App Scraping de Reviews do app Alexa na Google Play Store     #\n# 2- Limpeza e Filtragem de Dados                                  #\n# 3- Geração de 3 arquivos csv filtradas pela avaliação            #\n#    dos usuários                                                  #\n# 4- Geração de Reports de análise dos dados coletados             #\n# 5- Gravação de informações no banco de dados                     #\n# 6- Limpeza do diretório de origem dos arquivos CSV               #\n#                                                                  #\n####################################################################\n')
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