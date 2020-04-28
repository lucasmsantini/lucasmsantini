# teste API
import json

import requests


def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=26f9b1c0&t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('erro de conexão')
        return None


def print_detalhes(filme):
    print(filme['Title'])
    print(filme['Actors'])
    print(filme['Year'])
    print(filme['Plot'])


sair = False

while not sair:
    op = input('Digite o nome do filme ou [sair] para finalizar: ')
    if op == 'sair':
        sair = True
        print('Saiu do sistema')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            print_detalhes(filme)
