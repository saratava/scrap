import pandas as pd
import numpy as np
from google_play_scraper import Sort, reviews_all
from pandas_profiling import ProfileReport as pr
import os

# App Scraping Alexa - google play
br_reviews = reviews_all(
    'com.amazon.dee.app',
    lang='pt',
    sleep_milliseconds=0,
    country='br',
    sort=Sort.NEWEST,
)


print('_____________ Acionando o Tratamento de Dados _____________')
import tratamento



