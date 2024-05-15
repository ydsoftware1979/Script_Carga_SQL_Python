import pandas as pd
from faker import Faker
import random
from datetime import datetime

# Criação de instância da Faker
faker = Faker()

# Número de registros fictícios a serem gerados
num_records = 100

# Função para gerar dados fictícios e salvar em um arquivo Excel
def generate_and_save_fake_data(num_records, filename):
    """
    Generates fake data and saves it to an Excel file.

    Args:
        num_records: The number of fake records to generate.
        filename: The name of the Excel file to save the data.

    Returns:
        None
    """
    data = []
    for _ in range(num_records):
        nf = random.randint(1, 999999)
        fornecedor_id = random.randint(1, 999999)  # Gere IDs únicos (neste exemplo)
        nome = faker.name()
        emissao = faker.date_between(start_date='-1y', end_date='today')  # Data de emissão no último ano até hoje
        emissao_formatada = emissao.strftime('%d/%m/%Y')  # Formata a data para DD/MM/AAAA
        data.append({'fornecedor_id': fornecedor_id, 'name': nome, 'emissao': emissao_formatada})

        #data.append({'Nº NF': nf, 'fornecedor_id': fornecedor_id, 'name': nome})
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)






    #df = pd.DataFrame(data)
    #df.to_excel(filename, index=False)

# Gera dados fictícios e salva em um arquivo Excel
filename = 'dados_ficticios.xlsx'
generate_and_save_fake_data(num_records, filename)
print(f"{num_records} registros salvos com sucesso no arquivo {filename}!")
