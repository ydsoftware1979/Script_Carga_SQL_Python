Scripts de Geração de Dados Fictícios
Este repositório contém scripts em Python que geram e inserem dados fictícios em um banco de dados SQL Server usando a biblioteca pyodbc e a biblioteca Faker. Esses scripts são úteis para popular um banco de dados com dados de teste para fins de desenvolvimento e teste.

Scripts
generate_certificado_colaborador_data.py: Este script gera e insere dados fictícios na tabela certificado_colaborador. Ele gera duas linhas para cada registro, uma com uma data de validade um ano antes da data atual e outra com uma data de validade um ano após a data atual.

generate_certificado_colaborador_data_v2.py: Semelhante ao primeiro script, ele gera e insere dados fictícios na tabela certificado_colaborador. Ele gera duas linhas para cada registro, uma com uma data de validade um ano antes da data atual e outra com uma data de validade um ano após a data atual. Esta versão do script permite personalizar o número de registros fictícios a serem gerados.

generate_cliente_fornecedor_data.py: Este script gera e insere dados fictícios na tabela cliente_fornecedor. Ele gera registros aleatórios com valores de cliente_id e fornecedor_id entre 1 e 30.

Uso
Clone este repositório para a sua máquina local:

bash
Copy code
git clone https://github.com/seu-nome-de-usuário/seu-repo.git
Configure os detalhes da conexão com o banco de dados nos scripts, substituindo os valores fictícios para server, database, username e password pelos seus detalhes reais de conexão com o banco de dados.

Instale as bibliotecas necessárias usando o pip:

bash
Copy code
pip install pyodbc faker
Execute o(s) script(s) de sua escolha para gerar e inserir dados fictícios no seu banco de dados SQL Server.

Verifique se os dados foram inseridos com sucesso.

Dependências
pyodbc: Usado para a conexão com o banco de dados.
Faker: Usado para a geração de dados fictícios.
Licença
Este projeto está licenciado sob a Licença MIT. Sinta-se à vontade para usar e modificar os scripts conforme necessário para seus próprios projetos.

Não se esqueça de substituir "seu-nome-de-usuário/seu-repo" pela URL real do seu repositório no GitHub. Você pode expandir ainda mais este README fornecendo informações adicionais sobre o seu projeto, esquema do banco de dados ou instruções específicas de uso.