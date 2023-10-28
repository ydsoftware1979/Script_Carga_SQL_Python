# Fake Data Generation Scripts

This repository contains a set of Python scripts for generating and inserting fake data into a SQL Server database. These scripts are useful for testing and development purposes, allowing you to quickly populate your database with mock data.

## Scripts

### Script 1: `insert_fake_data.py`

- This script generates and inserts fake data into a SQL Server database using the `pyodbc` and `Faker` libraries.
- It creates fake records in the `certificado_colaborador` table with random `colaborador_id`, `certificado_id`, and `data_validade` values.

### Script 2: `insert_fake_data_fixed.py`

- Similar to the first script, this one generates and inserts fake data into a SQL Server database using the `pyodbc` and `Faker` libraries.
- It creates fake records in the `certificado_colaborador` table with fixed `colaborador_id` and `certificado_id` values and random `data_validade` values.

### Script 3: `insert_fake_data_cliente_fornecedor.py`

- This script generates and inserts fake data into a SQL Server database using the `pyodbc` library.
- It creates fake records in the `cliente_fornecedor` table with random `cliente_id` and `fornecedor_id` values.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
