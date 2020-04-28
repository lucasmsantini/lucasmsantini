import requests

try:
    requisicao = requests.get('http://www.g1.com.br/')
    print(requisicao.text)
except Exception as e:
    print('Erro na requisição:', e)
    