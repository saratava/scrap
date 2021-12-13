import mysql.connector
# from modules.manage_json import ManageJson


database = mysql.connector.connect(
    host="localhost", user="sarat", password="2708", database="mydatabase"
)

mycursor = database.cursor()

# sql = "DROP TABLE scrap"

# mycursor.execute(sql)

sql = "INSERT INTO scrap (content, score, thumbsUpCount, reviewCreatedVersion, at, replyContent, repliedAt) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = {}
# mycursor.execute(sql, val)

# database.commit()

# print(mycursor.rowcount, "record inserted.")

# mycursor.execute("CREATE TABLE scrap (id INT AUTO_INCREMENT PRIMARY KEY, content VARCHAR(300), score INT, thumbsUpCount INT, reviewCreatedVersion FLOAT, at DATETIME, replyContent VARCHAR(300), repliedAt DATETIME)")
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# for x in mycursor:
#   print(x)

print('deu certo')
# mycursor.execute("SHOW DATABASES")

        # for x in mycursor:
        #     print(x)
    # def extract_account_moviment(self, year, month, day):
    #     block_list_extract = ManageJson.load_anything("login")["block_list"]
    #     block_list_extract.append(9999)
    #     block_list_extract.append(9999)
    #     block_list = tuple(block_list_extract)

    #     """ Faz uma consulta no banco de dados na tabelas
    #     "movimento_conta" e depois formata essa saída em uma
    #     lista de dicionários. """
    #     cursor = self.database.cursor()
    #     cursor.execute(
    #         f""" 
    #     SELECT 
    #     Id,
    #     PessoaId,
    #     DataMovimento,
    #     DataVencimento,
    #     DataPagamento,
    #     Tipo,
    #     Valor,
	# 	SituacaoPagamento,
    #     NumeroParcela,
    #     TotalParcelas,
    #     Situacao,
    #     MovimentoNotaFiscalId
    #     FROM movimento_conta 
    #     WHERE (DataMovimento >= '{year}-{month}-{day} 00:00:00') AND 
    #     (SituacaoPagamento=0) AND (Situacao=0) AND (Tipo=0) AND PessoaId NOT IN {block_list}  ;"""
    #     )
    #     # parametros que estavam na query mas retirei
    #     # AND (SituacaoPagamento=0) AND (Situacao=0) AND Tipo=0
    #     account_moviment = list()
    #     for moviment in cursor.fetchall():

    #         account_moviment.append(
    #             {
    #                 "Id": moviment[0],
    #                 "PessoaId": moviment[1],
    #                 "DataMovimento": moviment[2],
    #                 "DataVencimento": moviment[3],
    #                 "DataPagamento": moviment[4],
    #                 "Tipo": moviment[5],
    #                 "Valor": moviment[6],
    #                 "SituacaoPagamento": moviment[7],
    #                 "NumeroParcela": moviment[8],
    #                 "TotalParcelas": moviment[9],
    #                 "Situacao": moviment[10],
    #                 "MovimentoNotaFiscalId": moviment[11]


    #             })
    #     return account_moviment

    # def extract_person(self):
    #     """ Faz uma consulta no banco de dados na tabela
    #     "pessoa" e depois formata essa saída em uma
    #     lista de dicionários. """
    #     cursor = self.database.cursor()
    #     cursor.execute(
    #         """ 
    #     SELECT 
    #     Id,
    #     TipoPessoa,
    #     RazaoSocial,
    #     Telefone,
    #     IsCliente,
    #     IsFornecedor,
    #     Ativo,
    #     Aniversario
    #     FROM pessoa WHERE IsCliente=1;"""
    #     )
    #     person = list()
    #     for item in cursor.fetchall():
    #         person.append({
    #             "PessoaId": item[0],
    #             "TipoPessoa": item[1],
    #             "RazaoSocial": item[2],
    #             "Telefone": item[3],
    #             "IsCliente": item[4],
    #             "IsFornecedor": item[5],
    #             "Ativo": item[6],
    #             "Aniversario": item[7],

    #         })
    #     return person
