import pymysql

config = {
    'user': 'sarat',  # nome do Usuário do Banco
    'host': 'localhost',  # nome do Host do Banco
    'password': '2708',  # senha do Banco
    'database': 'mydatabase'  # nome do banco de dados
}
cnx = pymysql.connect(**config, charset='utf8mb4')  # Conexão
cursor = cnx.cursor()

# cursor.execute("CREATE TABLE aval_positiva (id INT AUTO_INCREMENT PRIMARY KEY, content TEXT, score INT, thumbsUpCount INT, reviewCreatedVersion TEXT, at TIMESTAMP, replyContent TEXT)")
# cursor.execute("CREATE TABLE aval_negativa (id INT AUTO_INCREMENT PRIMARY KEY, content TEXT, score INT, thumbsUpCount INT, reviewCreatedVersion TEXT, at TIMESTAMP, replyContent TEXT)")
# cursor.execute("CREATE TABLE aval_neutra (id INT AUTO_INCREMENT PRIMARY KEY, content TEXT, score INT, thumbsUpCount INT, reviewCreatedVersion TEXT, at TIMESTAMP, replyContent TEXT)")
# cnx.commit()
# print('Tabelas Criadas')


# cursor.execute("DROP TABLE aval_positiva")
# cursor.execute("DROP TABLE aval_negativa")
# cursor.execute("DROP TABLE aval_neutra")
# cnx.commit()
# print('Tabelas apagadas')