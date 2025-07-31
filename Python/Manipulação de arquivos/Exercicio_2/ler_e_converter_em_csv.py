import pandas as pd

#ler arquivo excel
df = pd.read_excel('pedidos_ecommerce.xlsx')  # Use o nome correto do seu arquivo

#salvar os dados em CSV
df.to_csv('pedidos_ecommerce.csv', index=False)

print("Arquivo CSV criado com sucesso!")
