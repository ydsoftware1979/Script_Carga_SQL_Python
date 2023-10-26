import pyodbc
from faker import Faker
import random

# Configuração da conexão com o banco de dados SQL Server
server = 'Endereço_servidor_banco'
database = 'Banco_dadps'
username = 'Usuario_acesso'
password = 'Senha_Acesso'
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Criação de instância da Faker
faker = Faker()

num_records = 250

# Função para gerar e inserir dados fictícios na tabela
def insert_fake_data(connection, num_records):
    cursor = connection.cursor()
    for colaborador_id in range(1, num_records + 1):
        name = faker.name()
        fornecedor_id = random.randint(1, 250)  # Gere IDs aleatórios entre 1 e 250
        query = f"INSERT INTO colaborador (colaborador_id, name, fornecedor_id) VALUES ({colaborador_id}, '{name}', {fornecedor_id})"
        cursor.execute(query)
    connection.commit()

# Conecta ao banco de dados e insere os dados fictícios
try:
    conn = pyodbc.connect(connection_string)
    insert_fake_data(conn, num_records)
    print(f"{num_records} registros inseridos com sucesso!")
except Exception as e:
    print("Ocorreu um erro:", e)
finally:
    conn.close()