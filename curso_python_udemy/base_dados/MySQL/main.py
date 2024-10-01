import os
import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
# Define o tipo de cursor a ser usado. DictCursor retorna os resultados como dicionários
CURRENT_CURSOR = pymysql.cursors.DictCursor

# Carrega as variáveis de ambiente do arquivo .env
dotenv.load_dotenv()

# Conexão ao banco de dados MySQL usando variáveis do ambiente presentes no .env
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=CURRENT_CURSOR,
)

with connection: 
    with connection.cursor() as cursor:
        # Criação da tabela se não existir, com as colunas id, nome e idade
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )

        # Limpa a tabela, removendo todos os registros
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit() # Confirma as alterações no banco de dados

    # Inicio da manipulação de dados 

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) ' # Placeholders para nome e idade
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data)
        connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) ' # Placeholders para dicionários
        )
        data2 = {
            "name": "Luiza",
            "age": 27,
        }
        result = cursor.execute(sql, data2)
        connection.commit()

    # Inserindo vários valores usando placeholder e um iterável de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Suelen", "age": 33, },
            {"name": "Carlos", "age": 74, },
            {"name": "Amara", "age": 16, },
            {"name": "Lucas", "age": 41, },
        )
        result = cursor.executemany(sql, data3)
        connection.commit()    

    # Inserindo vários valores usando placeholder e tuplas de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Juan", 22 ),
            ("Rosa", 27 ),
        )
        result = cursor.executemany(sql, data4)
        connection.commit()     

    # Lendo os valores com SELECT    
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )
        cursor.execute(sql)

        # # Consulta de um dado
        # data5 = cursor.fetchone()
        # print(data5)

        # # Consulta vários
        # data6 = cursor.fetchall()
        # for row in data6:
        #     print(row)

    # Lendo valores com WHERE
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id > 5 '
        )
        cursor.execute(sql)
        # data7 = cursor.fetchall()
        # for row in data7:
        #     print(row)

    # Apagando valors com Delete, Where e Placeholders
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s '  # Placeholder para a condição WHERE
        )
        cursor.execute(sql, (1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        # for row in cursor.fetchall():
        #     print(row)

    # Atulizando a tabela com UPDATE, Where e Placeholders
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s '
        )
        cursor.execute(sql, ('João', 19, 7))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        for row in cursor.fetchall():
            print(row)

        # Trocando o cursor para retornar dicionarioss (DictCursor)
        # for row in cursor.fetchall():
        #     print(row['nome'])

        # Exibe o número de linhas retornadas pela consulta
        print(f'Linhas retornadas: {cursor.rowcount}')
