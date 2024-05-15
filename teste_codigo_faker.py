from faker import Faker
import random
faker = Faker('pt_BR')  # Use 'pt_BR' para dados brasileiros

Faker.seed(0)

categorias_produtos = ['alimentos', 'bebidas', 'cosméticos', 'eletrônicos', 'móveis']
produtos = []

for _ in range(10):
  categoria = random.choice(categorias_produtos)
  nome_produto = faker.word()
  produtos.append(f"{nome_produto} {categoria}")

# Cria uma lista com 100 instâncias dos produtos
produtos_repetidos = produtos * 10

# Embaralha a lista
random.shuffle(produtos_repetidos)

def generate_and_save_fake_data(num_records, filename):
  data = []

  for _ in range(100):  # Gere 100 linhas de dados
    fornecedor_id = random.randint(1, 999999)  # Gere IDs únicos (neste exemplo)
    nome = faker.name()
    emissao = faker.date_between(start_date='-1y', end_date='today')  # Data de emissão no último ano até hoje
    emissao_formatada = emissao.strftime('%d/%m/%Y')  # Formata a data para DD/MM/AAAA
    cnpj = faker.cnpj()
    contrato = faker.word()
    valor_sedex = round(random.uniform(10, 100), 2)  # Valores financeiros entre 10,00 e 100,00
    status = faker.http_status_code()

    # Seleciona um produto aleatório da lista
    produto = random.choice(produtos_repetidos)

    data.append({
      'Nº NF': fornecedor_id,
      'emissao': emissao_formatada,
      'Cliente': nome,
      'CNPJ': cnpj,
      'QUANT.': contrato,
      'CÓD.': 'null',
      'Produto': produto,
      'Valor Sedex': valor_sedex,
      'Status': status
    })

  df = pd.DataFrame(data)
  df.to_excel(filename, index=False)
    df.to_excel(filename, index=False)
