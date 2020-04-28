# https://www.youtube.com/watch?v=2Co4cjPMTnk&list=PLp95aw034Wn_WtEmlepaDrw8FU8R5azcm&index=12
# https://putsreq.com/4065hdVOGOpcJvOaUIRx
import requests


cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'http://www.siteinexistente.com.br'}
texto = None
try:
    requisicao = requests.post('https://putsreq.com/uiIrN58xcNLQNpoTH9At',
                               headers=cabecalho)
    texto = requisicao.text
except Exception as e:
    print("requisição com erro:", e)
print(texto)
