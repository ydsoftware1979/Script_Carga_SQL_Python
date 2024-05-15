import pandas as pd
from faker import Faker
import random

# Criação de instância da Faker
faker = Faker('pt_BR')  # Use 'pt_BR' para dados brasileiros

# Número de registros fictícios a serem gerados
num_records = 500

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

# Função para gerar dados fictícios
def generate_fake_data():
  data = []
  for _ in range(num_records):
    nf = random.randint(1, 999999)
    emissao = faker.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
    cnpj = generate_fake_cnpj()
    valor_financeiro = round(random.uniform(100, 10000), 2)
    qtd = random.randint(1, 99)
    cod = random.randint(1, 99)
    endereco = faker.address()
    empresa = faker.company()
    cidade = faker.city()
    fornecedor_id = random.randint(1, 999999)
    nome = faker.name()
    produto = faker.word()
    contrato = faker.word()
    valor_sedex = round(random.uniform(10, 100), 2)
    lote_number  = random.randint(10, 19)
    bobina = random.randint(1, 9)
    solicitacao = random.randint(10, 99)
    desconto = random.randint(0, 15)
    emissao2 = faker.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
    remessa = random.randint(1, 999999)
    saida_material = random.choice(['Retira', 'Sedex'])
    produtos = random.choice(['Produto IPEM', 'Produto IMETRO', 'Produto Selo', 'Produto Seguro', 'Selo Seguranca', 'Selo lacre', 'Selo Inspeção'])
    codigo = random.randint(145, 172)
    status =  random.choice(['Status 1', 'Status 2', 'Status 3', 'Status 4', 'Status 5'])

    data.append({
      'Nº NF': nf, 
      'emissao': emissao,
      'Cliente': empresa, 
      'CNPJ': cnpj,
      'QUANT.': qtd,
      'CÓD.': codigo,
      'Produto' : produtos,
      'Contrato' : contrato,
      'VALOR':  valor_financeiro,
      'SEDEX PAGO PELO CLIENTE ': valor_sedex,
      'TOTAL COM SEDEX': (valor_financeiro + valor_sedex),
      'Status' : status,
      'DATA PAGTO DO CLIENTE': emissao2,
      'VALOR PAGO PELO CLIENTE': round((valor_financeiro + valor_sedex) - ((valor_financeiro + valor_sedex)*(desconto / 100)), 2),
      'SAIDA DO MATERIAL RETIRA / SEDEX': saida_material,
      'NOTA DE REMESSA': remessa,
      'SOLICITAÇÃO': solicitacao,
      'LOTE': '2023/' + str(lote_number),
      'BOBINA': bobina,
    })

  return pd.DataFrame(data)

# Função para salvar dados fictícios em um arquivo Excel
def save_data_to_excel(data, filename):
  # Estilo de formatação para adicionar bordas
  border_style = {
    'border': '1px solid black'
  }
  header_style = {
    'border': '1px solid black',
    'font-weight': 'bold',
    'text-align': 'center'
  }

  # Aplicar estilos às células
  styled_df = data.style \
    .set_properties(**border_style) \
    .set_properties(subset=[data.columns[0]], **header_style)  # Aplica estilo ao cabeçalho

  # Salvar para Excel
  styled_df.to_excel(filename, index=False)

# Gera dados fictícios
fake_data = generate_fake_data()

# Salva dados fictícios em um arquivo Excel
filename = 'dados_ficticios.xlsx'
save_data_to_excel(fake_data, filename)

print(f"{num_records} registros salvos com sucesso no arquivo {filename}!")
