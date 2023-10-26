import pyodbc
from faker import Faker
import random
from datetime import datetime, timedelta

# Configuração da conexão com o banco de dados SQL Server
server = 'Endereço_servidor_banco'
database = 'Banco_dadps'
username = 'Usuario_acesso'
password = 'Senha_Acesso'
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Criação de instância da Faker
faker = Faker()

# Número de registros fictícios a serem gerados
num_records = 3500

# Função para gerar e inserir dados fictícios na tabela
def insert_fake_data(connection, num_records):
    cursor = connection.cursor()
    today = datetime.today()
    for id in range(1, num_records + 1):
        colaborador_id = random.randint(1, 30)
        certificado_id = random.randint(1, 30)
        
        # Um ano antes
        random_days_before = random.randint(1, 365)  # Intervalo de até 1 ano
        data_validade_before = (today - timedelta(days=random_days_before + 365)).strftime('%Y-%m-%d %H:%M:%S')
        
        # Um ano depois
        random_days_after = random.randint(1, 365)  # Intervalo de até 1 ano
        data_validade_after = (today + timedelta(days=random_days_after + 365)).strftime('%Y-%m-%d %H:%M:%S')
        
        query = f"INSERT INTO certificado_colaborador (id, colaborador_id, certificado_id, data_validade) VALUES ({id}, {colaborador_id}, {certificado_id}, '{data_validade_before}')"
        cursor.execute(query)
        
        query = f"INSERT INTO certificado_colaborador (id, colaborador_id, certificado_id, data_validade) VALUES ({id}, {colaborador_id}, {certificado_id}, '{data_validade_after}')"
        cursor.execute(query)
        
    connection.commit()

# Conecta ao banco de dados e insere os dados fictícios
try:
    conn = pyodbc.connect(connection_string)
    insert_fake_data(conn, num_records)
    print(f"{num_records * 2} registros inseridos com sucesso!")
except Exception as e:
    print("Ocorreu um erro:", e)
finally:
    conn.close()
