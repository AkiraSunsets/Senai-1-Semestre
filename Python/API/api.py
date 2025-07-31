import requests 

response = requests.get("https://ponyapi.net/v1/character/4")

personagem = response.json()

nome_personagem = personagem["data"][0]["name"]
# 0 = id, 
# name = mostra o nome do personagem, 
# data = busca todo o conteudo dentro daquela chave

print(nome_personagem)


#
API - integrar dois sistemas
ex: back e front-end

API rest:
transferencia de estado representacional
salva o estado 

Endpoint:
local da API onde um sistema interage com uma API da web, Ponto de comunicação entre dois sistemas

criar pasta -> entrar -> abrir terminal -> 
coloca o comando: py -m venv env  //cria uma pasta com o nome "env"

cd env -> cd .\Scripts\ -> .\activate -> pip install (a biblioteca que vc quer instalar) 

pip freeze // para ver quais bibliotecas estão instaladas e suas versões

pip freeze > requirements.txt \\criar um txt com as bibliotecas instaladas 

pip install -r .\requirements.txt \\instalar bibliotecas a partir de txt
#
