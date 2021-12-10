from google_play_scraper import app
import pandas as pd
import numpy as np
from google_play_scraper import Sort, reviews_all


us_reviews = reviews_all(
    'com.amazon.dee.app',
    lang='pt',  # defaults to 0
    sleep_milliseconds=0,  # defaults to 'en'
    country='br',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
)

df_busu = pd.DataFrame(np.array(us_reviews), columns=['review'])


df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))


print(df_busu)


