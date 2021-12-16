import pandas as pd
import numpy as np
from google_play_scraper import Sort, reviews_all
from pandas_profiling import ProfileReport as pr
import os


# App Scraping Alexa - google play
br_reviews = reviews_all(
    'org.telegram.messenger',
    lang='pt',
    sleep_milliseconds=0,
    country='br',
    sort=Sort.NEWEST,
)

# Geração de DataFrame do atributo Review do App Alexa
df_reviews = pd.DataFrame(np.array(br_reviews), columns=['review'])

df_completa = df_reviews.join(pd.DataFrame(df_reviews.pop('review').tolist()))

df_final = df_completa.drop(columns=['reviewId','userName','userImage', 'repliedAt'])

# Filtragem de acordo com o score (estrelas) atribuida
filtro_positiva = df_final['score'] >= 4
df_positiva = df_final[filtro_positiva]

filtro_neutra = df_final['score'] == 3
df_neutra = df_final[filtro_neutra]

filtro_negativa = df_final['score'] < 3
df_negativa = df_final[filtro_negativa]

path = os.getcwd()

# Report Positivas
profile_positivo = pr(df_positiva, title='Report Geral Reviews Alexa - Avaliações Positivas', html={'style':{'full_width':True}})

profile_positivo.to_notebook_iframe()

profile_positivo.to_file(output_file=f"{path}/Report_Positivas.html")
profile_positivo.to_file(output_file=f"{path}/backup_report/Report_Positivas.html")

# Report Neutras
profile_neutra = pr(df_neutra, title='Report Geral Reviews Alexa - Avaliações Neutras', html={'style':{'full_width':True}})

profile_neutra.to_notebook_iframe()

profile_neutra.to_file(output_file=f"{path}/Report_Neutras.html")
profile_positivo.to_file(output_file=f"{path}/backup_report/Report_Neutras.html")

# Report Negativas
profile_negativa = pr(df_negativa, title='Report Geral Reviews Alexa - Avaliações Negativas', html={'style':{'full_width':True}})

profile_negativa.to_notebook_iframe()

profile_negativa.to_file(output_file=f"{path}/Report_Negativas.html")
profile_positivo.to_file(output_file=f"{path}/backup_report/Report_Negativas.html")

df_positiva.to_csv(f"{path}/df_positiva.csv", index=False)               
df_neutra.to_csv(f"{path}/df_neutra.csv", index=False)                   
df_negativa.to_csv(f"{path}/df_negativa.csv", index=False) 

df_positiva.to_csv(f"{path}/backup_csv/df_positiva.csv", index=False)               
df_neutra.to_csv(f"{path}/backup_csv/df_neutra.csv", index=False)                   
df_negativa.to_csv(f"{path}/backup_csv/df_negativa.csv", index=False) 

print('_____________ Acionando o Banco _____________')

# import request_database
# print(request_database)