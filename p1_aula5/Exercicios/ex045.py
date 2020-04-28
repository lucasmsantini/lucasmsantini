from random import randint
from time import sleep

print('PEDRA, PAPEL ou TESOURA?')
itens = ('PEDRA', 'PAPEL', 'TESOURA')

print('''Opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Digite a sua escolha: '))

comp = randint(0,2)
print('Você escolheu: {}'.format(itens[op]))
print('O computador jogou: {}'.format(itens[comp]))

if comp == 0: #-------------pedra
    if op == 0:
        print('Empatou')
    elif op == 1:
        print('Você ganhou')
    elif op == 2:
        print('Computador ganhou')
    else:
        print('Jogada Inválida')
elif comp == 1: #----------papel
    if op == 0:
        print('Computador ganhou')
    elif op == 1:
        print('Empatou')
    elif op == 2:
       print('Você ganhou')
    else:
        print('Jogada inválida')
else: #--------------------tesoura
    if op == 0:
        print('Você ganhou')
    elif op == 1:
        print('Computador ganhou')
    elif op == 2:
        print('Empatou')
    else:
        print('Jogada inválida')
