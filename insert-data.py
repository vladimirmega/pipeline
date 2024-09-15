import random
from faker import Faker

# Inicializando Faker para gerar dados aleatórios
fake = Faker()

# Função para gerar uma linha de valores para a tabela 'vendas'
def generate_random_sales_data():
    email = fake.email()
    data = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')  # Formatando o datetime
    valor = round(random.uniform(10.0, 1000.0), 2)  # Valor aleatório entre 10 e 1000
    quantidade = random.randint(1, 100)  # Quantidade aleatória entre 1 e 100
    produto = random.choice(["ZapFlow com Gemini", "ZapFlow com chatGPT","ZapFlow com Llama3.0"])  # Produto aleatório
    return f"('{email}', '{data}', {valor}, {quantidade}, '{produto}')"

# Gerando 1000 linhas de dados
lines = []
for _ in range(1000):
    lines.append(f"INSERT INTO public.vendas(email, data, valor, quantidade, produto)\nVALUES {generate_random_sales_data()};")

# Salvando no arquivo
file_path = '/home/vladimir/Estudos/pipeline/insert_data.sql'
with open(file_path, 'w') as file:
    file.write('\n'.join(lines))

file_path
