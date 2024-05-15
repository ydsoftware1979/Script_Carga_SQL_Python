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

# Exibe cada produto 10 vezes
for produto in produtos:
    for _ in range(10):
        print(produto)