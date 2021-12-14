from raspagem.scrap import etc


def database():   
    import csv
    import pymysql


    config={
        'user':'sarat', #nome do Usuário do Banco
        'host':'localhost', #nome do Host do Banco
        'password':'2708', #senha do Banco
        'database':'mydatabase'#nome do banco de dados
        }

    cnx = pymysql.connect(**config, charset='utf8mb4') #Conexão
    cursor = cnx.cursor() #Executar as querys

    input_file = csv.DictReader(open("sheets/df_negativa.csv", encoding='utf-8'))

    for row in input_file:

        cursor.execute("insert into mydatabase.aval_negativa (content, score, thumbsUpCount, reviewCreatedVersion, at, replyContent) \
        values (%s, %s, %s, %s, %s, %s)",(row['content'],row['score'],row['thumbsUpCount'],row['reviewCreatedVersion'],
        row['at'],row['replyContent']))

        # cursor.execute("CREATE TABLE aval_negativa (id INT AUTO_INCREMENT PRIMARY KEY, content VARCHAR(1000), score INT, thumbsUpCount INT, reviewCreatedVersion VARCHAR(100), at TIMESTAMP, replyContent VARCHAR(1000))")

        # cursor.execute("DROP TABLE aval_negativa")

        # cursor.execute("ALTER TABLE scrap CHANGE content content VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")

        # cursor.execute("OPTIMIZE TABLE scrap")

        # cursor.execute("SELECT * FROM aval_negativa WHERE score =2")
        # for x in cursor:
        #     print(x)

        cnx.commit()

etc()
