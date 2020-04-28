# requisicao = requests.get('http://www.g1.com.br/')

import requests


cabecalho = {'User-agent': 'Windows 12'}
texto = None
try:
    requisicao = requests.post('http://www.g1.com.br/', headers=cabecalho)
    texto = requisicao.text
except Exception as e:
    print("requisição com erro:", e)
print(texto)
