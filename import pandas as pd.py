import pandas as pd
import numpy as np
from faker import Faker

# Definindo o número de linhas
num_rows = 500

# Criação de instância da Faker
faker = Faker()

# Gerando os dados falsos
data = {
    "Nº NF": np.arange(10001, 10001 + num_rows),
    "EMISSÃO": pd.date_range(start="2023-01-01", periods=num_rows, freq='D').strftime('%d/%m/%Y'),
    "CLIENTE": [f"Empresa {chr(65 + i % 26)}" for i in range(num_rows)],
    "CNPJ": [f"{np.random.randint(10000000, 99999999)}0001{np.random.randint(10, 99)}" for _ in range(num_rows)],
    "QUANT.": np.random.randint(1, 100, size=num_rows),
    "CÓD.": np.random.randint(101, 200, size=num_rows),
    "PRODUTO": [f"Produto {chr(65 + i % 26)}" for i in range(num_rows)],
    "CONTRATO": [f"Contrato {chr(65 + i % 26)}" for i in range(num_rows)],
    "VALOR": np.round(np.random.uniform(100, 10000, size=num_rows), 2),
    "SEDEX PAGO PELO CLIENTE": np.round(np.random.uniform(10, 500, size=num_rows), 2),
    "TOTAL COM SEDEX": np.round(np.random.uniform(110, 10500, size=num_rows), 2),
    "STATUS": np.random.choice(["Pago", "Pendente"], size=num_rows),
    "DATA PAGTO DO CLIENTE": pd.date_range(start="2023-01-02", periods=num_rows, freq='D').strftime('%d/%m/%Y'),
    "VALOR PAGO PELO CLIENTE": np.round(np.random.uniform(110, 10500, size=num_rows), 2),
    "SAIDA DO MATERIAL RETIRA / SEDEX": np.random.choice(["Retira", "Sedex"], size=num_rows),
    "NOTA DE REMESSA": np.arange(20001, 20001 + num_rows),
    "SOLICITAÇÃO": np.arange(3001, 3001 + num_rows),
    "LOTE": [f"{2023}/{str(i).zfill(3)}" for i in range(num_rows)],
    "BOBINA": [f"{chr(65 + i % 26)}{np.random.randint(1, 10)}{chr(66 + i % 26)}{np.random.randint(1, 10)}" for i in range(num_rows)]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando em um arquivo CSV
df.to_csv("dados_fakes_empresa.csv", index=False)
