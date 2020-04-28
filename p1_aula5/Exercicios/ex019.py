import random
a = input('nome1: ')
b = input('nome2: ')
c = input('nome3: ')
d = input('nome4: ')
lista = [a,b,c,d]
escolhido = random.choice(lista)
print('O escolhido é: {}'.format(escolhido))