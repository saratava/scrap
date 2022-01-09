Instruções windows:

Dentro de C:\Users\<seu-usuario>\ faça o diretório onde trabalhará Sugestão de nome: scrap
ex. do caminho: C:\Users\sara\scrap

Instruções Linux:
Faça o diretório onde trabalhará Sugestão de nome: scrap
ex. do caminho: sara@sara:~/Área de Trabalho/scrap


Dentro de scrap faremos mais uma pasta "main". É dentro de main que faremos o git clone deste repositório.
Resultado final do caminho: C:\Users\sara\scrap\main
Certifique-se de estar igual.

Execute o VS Code a partir de main. 
A estrutura de pastas no VS Code deve ser:

SCRAP
    |_
      MAIN

Abra o terminal e execute:
'''
git clone https://github.com/saractavares/scraping-python-google-play-scraper.git
'''
Espere terminar.

Agora precisará executar a Venv. No terminal, digite e execute:

Windows:
'''
scrap-env-win\Scripts\Activate.ps1
'''

Linux:
'''
source scrap-env/bin/activate
'''

Agora adicionaremos as bibliotecas necessárias:
No terminal execute essa sequência, aguardando entre uma instalção e outra, claro:
'''
pip install google_play_scraper
'''
'''
pip install pandas
'''
Atenção: Numpy é instalado junto com Pandas, no comando acima.

'''
pip install pandas_profiling
'''
'''
pip install google-auth
'''
'''
pip install pandas_gbq
'''

Bibliotecas extras para evitar engasgos:
'''
pip install IPython
'''
'''
pip install ipywidgets
'''

Atenção: Se mesmo após as instalações, o código ainda reclamar que não há a biblioteca, certifique-se
de estar usando a mesma versão python, nesse caso é a 3.8.10 Você pode conferir isso no canto inferior esquerdo da janela do VsCode.
Sempre recomendo reiniciar o Vs Code após a instalação das bibliotecas.

Podemos agora seguir para a parte do banco de dados. Para conseguir subir as tabelas, você precisará das credenciais de acesso. É o arquivo scrap-sauter-b84203485905.json que foi enviado no email.

A chave deve estar dentro da pasta "credentials", dentro de "database". Se não estiver, faça.
A estrutura final deve ser:

Windows:
'''
C:\Users\sara\scrap\main\scraping-python-google-play-scraper\database\credentials\scrap-sauter-b84203485905.json
'''

Linux:
'''
/home/sara/Área de Trabalho/scrap/main/scraping-python-google-play-scraper/database/credentials/scrap-sauter-b84203485905.json
'''


Por padrão, o repositório no github não tráz as pastas de backup pois as adicionamos ao gitignore, então as faremos também. Dentro de scraping-python-google-play-scraper faça as pastas "page_backup" e "tables_backup".

A estrutura será:

> SCRAP
    |_
    > MAIN
        |_
        > scraping-python-google-play-scraper
              |_
              > page_backup
              > tables_backup
              > database
                    |_
                    > credentials
              ...
          
Sem mais delongas, hora de rodar!
Abra o módulo scrap.py e execute!

O fluxo da execução é:

'''
1º scrap.py          -> faz -> scraping por meio da lib google-play-scraper
                     -> invoca -> tratamento.py

2º tratamento.py     -> faz -> limpeza dos dados coletados e organização por score
                     -> invoca -> file_factory.py

3º file_factory.py   -> faz -> 3 arquivos html de report usando a lib pandas-profiling
                     -> invoca -> drop.py

4º drop.py -> faz    -> checagem se existe já tabelas no banco de dados, se sim, as apaga
           -> invoca -> insert_tables.py

5º insert_tables.py  -> faz -> inserção dos arquivos csv nas tabelas correspondentes por meio de pandas_gbq
                     -> invoca -> limpar.py

6º limpar.py         -> faz -> limpeza dos arquivos csv já consumidos da raiz local

--- Fim do Processo ---
'''

