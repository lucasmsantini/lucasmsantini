# https://www.youtube.com/watch?v=2Co4cjPMTnk&list=PLp95aw034Wn_WtEmlepaDrw8FU8R5azcm&index=12

import requests


cabecalho = {'User-agent': 'Windows 12'}
texto = None
try:
    requisicao = requests.post('http://www.g1.com.br/', headers=cabecalho)
    texto = requisicao.text
except Exception as e:
    print("requisição com erro:", e)
print(texto)
