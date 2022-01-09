 
Fazer a Venv:
python3 -m venv scrap-env

Iniciar a Venv:
source scrap-env/bin/activate

"""
é necessário a pessoa fazer localmente a pasta raiz > main > scraping-python-google-play-scraper
ou
colocar isso no yml
"""


python -m venv C:\Users\ttava\scrap\main\scraping-python-google-play-scraper\scrap-env-win

instruções windows:

Dentro de C:\Users\<seu-usuario>\ faça o diretório onde trabalhará Sugestão de nome: scrap
ex. do caminho: C:\Users\sara\scrap

Dentro de scrap faremos mais uma pasta "main". É dentro de main que faremos o git clone deste repositório.
Resultado final do caminho: C:\Users\sara\scrap\main
Certifique-se de estar igual.

Execute o VS Code a partir de main. 
Abra o terminal e execute:
'''
git clone https://github.com/saractavares/scraping-python-google-play-scraper.git
'''

Espere terminar.

Agora precisará executar a Venv. No terminal, digite e execute:
'''
scrap-env-win\Scripts\Activate.ps1
'''

Agora adicionaremos as bibliotecas necessárias:
No terminal execute essa sequência, aguardando entre uma instalção e outra, claro:
'''
pip install google_play_scraper
'''
'''
pip install pandas
'''
'''
pip install numpy
'''
'''
pip install pandas_profiling
'''
'''
pip install google-auth
'''
'''
pip install pandas_gbq
'''