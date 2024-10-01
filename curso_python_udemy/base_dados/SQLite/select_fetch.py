import sqlite3
from main import DB_FILE, TABLE_NAME

# Estabelece a conexão com o banco de dados
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Executa uma consulta para selecionar todos os registros da tabela
cursor.execute(f'SELECT * FROM {TABLE_NAME}')

# Itera sobre os resultados e imprime cada linha da tabela
print('Todas as linhas da tabela')
for row in cursor.fetchall():
    customers_id, name, weight = row
    print(customers_id, name, weight)

print()

# Executa uma consulta para selecionar o registro com id = 1
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = 1'
)
row = cursor.fetchone()
customers_id, name, weight = row
print('Linha do ID 1')
print(customers_id, name, weight)

# Fecha o cursor e a conexão
cursor.close()
connection.close()