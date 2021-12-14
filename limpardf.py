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

print('_____________ Limpeza Concluída _____________')
# import request_database
# print(request_database.database)

# /home/sarat/Área de Trabalho/scraping-python-google-play-scraper/sheets