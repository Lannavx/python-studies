import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent  # Define o diretório raiz com base no caminho do arquivo atual
DB_NAME = 'db.sqlite3'  # Define o nome do arquivo do banco de dados
DB_FILE = ROOT_DIR / DB_NAME  # Cria o caminho completo para o arquivo de banco de dados
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE) # Estabelece a conexão com o banco de dados
cursor = connection.cursor() # Cria um cursor para executar comandos SQL

# CRUD - Create  Read   Update  Delete
# SQL  - INSERT  SELECT  UPDATE  DELETE

# Deleta todos os registros da tabela sem filtro (sem WHERE)
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Remove a sequência de autoincremento associada à tabela no sistema interno do SQLite
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela se ela ainda não existir
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL' 
    ')'
)
connection.commit()

# Registra múltiplos valores nas colunas da tabela utilizando placeholders
user_data = [
    (None, "Ana Maria", 9.9),  # Usando None para o id ser autoincrementado
    (None, "Helena", 4),
    (None, "Lucas", 10),
    (None, 'Joana', 5)
]

# Insere múltiplos registros de forma segura com executemany e placeholders (?, ?, ?)
cursor.executemany(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) VALUES (?, ?, ?)',
    user_data  # Lista de tuplas com os valores
)
connection.commit()

# Este bloco será executado apenas se o arquivo for executado diretamente
if __name__ == '__main__':

    # Executa uma consulta SQL para deletar o registro onde o id é igual a 3
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 3'
    )
    connection.commit()

    # Executa uma consulta SQL para atualizar o nome e o peso do registro onde o id é igual a 2
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name = "Exemplo", weight = 67.89 '
        'WHERE id = 2'
    )
    connection.commit()

    # Executa uma consulta para selecionar todos os registros da tabela
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')

    # Itera sobre os resultados e imprime cada linha
    for row in cursor.fetchall():
        customers_id, name, weight = row
        print(customers_id, name, weight)

    # Fecha o cursor e a conexão com o banco de dados após as operações
    cursor.close()
    connection.close()