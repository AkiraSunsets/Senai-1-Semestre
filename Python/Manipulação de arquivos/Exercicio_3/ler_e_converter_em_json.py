import pandas as pd

#ler o arquivo csv
df = pd.read_csv('pedidos_ecommerce.csv', sep=';')

#converter para JSON
df.to_json('pedidos_ecommerce.json', orient='records', force_ascii=False, indent=4)

print("Arquivo JSON criado com sucesso!")
