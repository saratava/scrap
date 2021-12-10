# from google_play_scraper import app
import pandas as pd
import numpy as np
from google_play_scraper import Sort, reviews_all


br_reviews = reviews_all(
    'com.amazon.dee.app',
    lang='pt',  # defaults to 'en'
    sleep_milliseconds=0,  # defaults to 0
    country='br',  # defaults to 'us'
    sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
)

df_reviews = pd.DataFrame(np.array(br_reviews), columns=['review'])

df_completa = df_reviews.join(pd.DataFrame(df_reviews.pop('review').tolist()))

df_final = df_completa.drop(columns=['reviewId','userName','userImage'])

filtro_positiva = df_final['score'] >= 4
df_positiva = df_final[filtro_positiva]

filtro_neutra = df_final['score'] == 3
df_neutra = df_final[filtro_neutra]

filtro_negativa = df_final['score'] < 3
df_negativa = df_final[filtro_negativa]


# df_busu.to_excel("scraping_com_python.xlsx", index=False)
# df_completa.head()
# df_final.to_excel("scraping_com_python-limpa.xlsx", index=False)

# print(df_positiva)
# print()
# print(df_neutra.to_csv)
# print()
# print(df_negativa)

# df_positiva.to_csv("df_positiva.csv", index=False)
# df_neutra.to_csv("df_neutra.csv", index=False)
# df_negativa.to_csv("df_negativa.csv", index=False)
import IPython.core.display
from pandas_profiling import ProfileReport as pr

profile = pr(df_final, title='Report Geral Reviews Alexa', html={'style':{'full_width':True}})

profile.to_notebook_iframe()

profile.to_file(output_file="/home/sarat/Área de Trabalho/scraping-python-google-play-scraper/Report_Scraping_Alexa.html")