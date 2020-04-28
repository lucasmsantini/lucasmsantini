print('='*20, 'Mega Sena', '='*20, )
from random import randint
lista = list()
jogos = []
cont = 0
quant = int(input('Quantos jogos deseja mostrar? '))
tot = 0
for i in range(0,quant):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    print(jogos)

