import pyodbc
from faker import Faker
import random

# Configuração da conexão com o banco de dados SQL Server
server = 'ec2-3-83-174-1.compute-1.amazonaws.com'
database = 'teste_alex'
username = 'sa'
password = 'G@308VITBDGDfg'
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'



# Criação de instância da Faker
faker = Faker()

# Número de registros fictícios a serem gerados

num_records = 100

# Função para gerar e inserir dados fictícios na tabela
def insert_fake_data(connection, num_records):
    cursor = connection.cursor()
    for _ in range(num_records):
        fornecedor_id = random.randint(1, 999999)  # Gere IDs únicos (neste exemplo)
        nome = faker.name()
        query = f"INSERT INTO fornecedor(fornecedor_id, name) VALUES ({fornecedor_id}, '{name}')"
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
