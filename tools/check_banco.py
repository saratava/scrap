import pymysql

config = {
    'user': 'sarat',  # nome do Usuário do Banco
    'host': 'localhost',  # nome do Host do Banco
    'password': '2708',  # senha do Banco
    'database': 'mydatabase'  # nome do banco de dados
}

cnx = pymysql.connect(**config, charset='utf8mb4')  # Conexão
cursor = cnx.cursor()  # Executar as querys

cursor.execute("SELECT * FROM aval_positiva WHERE score =4")
for x in cursor:
    print(x)
