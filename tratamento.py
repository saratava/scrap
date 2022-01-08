import pandas as pd
import numpy as np
from scrap import br_reviews


df_reviews = pd.DataFrame(np.array(br_reviews), columns=['review'])
df_completa = df_reviews.join(pd.DataFrame(df_reviews.pop('review').tolist()))
df_final = df_completa.drop(columns=['reviewId', 'userName', 'userImage', 'repliedAt'], axis=1)

# transformando os types
df = df_final.astype({"content": str, "score": int, "thumbsUpCount": int, "reviewCreatedVersion": str, 'at': int, "replyContent": str})

# Filtragem conforme o score (estrelas) atribuído
filtro_positiva = df_final['score'] >= 4
df_positiva = df_final[filtro_positiva]

filtro_neutra = df_final['score'] == 3
df_neutra = df_final[filtro_neutra]

filtro_negativa = df_final['score'] < 3
df_negativa = df_final[filtro_negativa]

# Retirando linhas com score null


print('_____________ Acionando a Fábrica de Arquivos _____________')
import file_factory


