from random import randint
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)
        }
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou: [{v}]')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
