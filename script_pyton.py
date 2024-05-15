import pandas as pd
from faker import Faker
import random
from datetime import datetime

# Criação de instância da Faker
faker = Faker()

# Número de registros fictícios a serem gerados
num_records = 100

# Função para gerar CNPJ fictício formatado
def generate_fake_cnpj():
    """
    Generates a fake CNPJ with the correct format.

    Returns:
        str: A string representing a fake CNPJ.
    """
    def calculate_cnpj_digit(cnpj):
        weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        total = sum(int(n) * weight[i] for i, n in enumerate(cnpj))
        remainder = total % 11
        return '0' if remainder < 2 else str(11 - remainder)
    
    base_cnpj = ''.join([str(random.randint(0, 9)) for _ in range(8)]) + '0001'
    first_digit = calculate_cnpj_digit(base_cnpj)
    second_digit = calculate_cnpj_digit(base_cnpj + first_digit)
    return f"{base_cnpj[:2]}.{base_cnpj[2:5]}.{base_cnpj[5:8]}/{base_cnpj[8:12]}-{first_digit}{second_digit}"


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
        emissao = faker.date_between(start_date='-1y', end_date='today')  # Data de emissão no último ano até hoje
        emissao_formatada = emissao.strftime('%d/%m/%Y')  # Formata a data para DD/MM/AAAA
        cnpj = generate_fake_cnpj()
        valor_financeiro = round(random.uniform(100, 10000), 2)  # Valores financeiros entre 100,00 e 10000,00

        empresa = faker.company()
        fornecedor_id = random.randint(1, 999999)  # Gere IDs únicos (neste exemplo)
        nome = faker.name()
        emissao = faker.date_between(start_date='-1y', end_date='today')  # Data de emissão no último ano até hoje
        emissao_formatada = emissao.strftime('%d/%m/%Y')  # Formata a data para DD/MM/AAAA
        
        
        
        
        data.append({
            'Nº NF': nf, 
            'emissao': emissao_formatada,
            'Cliente': empresa, 
            'CNPJ': cnpj,
            'name': nome, 
            'VALOR':  valor_financeiro
            
            
        })

        #data.append({'Nº NF': nf, 'fornecedor_id': fornecedor_id, 'name': nome})
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)






    #df = pd.DataFrame(data)
    #df.to_excel(filename, index=False)

# Gera dados fictícios e salva em um arquivo Excel
filename = 'dados_ficticios.xlsx'
generate_and_save_fake_data(num_records, filename)
print(f"{num_records} registros salvos com sucesso no arquivo {filename}!")
