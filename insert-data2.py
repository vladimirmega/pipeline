import random
from faker import Faker

# Inicializando Faker para gerar dados aleatórios
fake = Faker()

# Corrigindo o formato da data para garantir que seja corretamente interpretado pela função
from datetime import datetime

# Função para gerar dados de vendas com data entre 11/09/2024 e 15/09/2024 no formato especificado
def generate_random_sales_data_with_specific_date_range():
    email = fake.email()
    start_date = datetime(2024, 9, 11)
    end_date = datetime(2024, 9, 15)
    data = fake.date_time_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d %H:%M:%S')  # Definindo o intervalo de datas
    valor = round(random.uniform(10.0, 1000.0), 2)  # Valor aleatório entre 10 e 1000
    quantidade = random.randint(1, 100)  # Quantidade aleatória entre 1 e 100
    produto = random.choice(['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'])  # Produto aleatório
    return f"('{email}', '{data}', {valor}, {quantidade}, '{produto}')"

# Gerando 300 linhas de dados com datetime entre 11/09/2024 e 15/09/2024
lines_with_specific_date_range = []
for _ in range(300):
    lines_with_specific_date_range.append(f"INSERT INTO public.vendas(email, data, valor, quantidade, produto)\nVALUES {generate_random_sales_data_with_specific_date_range()};")

# Salvando no arquivo
file_path_with_specific_date_range = '/home/vladimir/Estudos/pipeline/insert_data_2.sql'
with open(file_path_with_specific_date_range, 'w') as file:
    file.write('\n'.join(lines_with_specific_date_range))

file_path_with_specific_date_range
