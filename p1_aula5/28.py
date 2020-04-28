from random import randint
numero1 = (randint(0,3))
numero2 = int(input('Qual o número que o computador pensou? '))
if numero1 == numero2:
    print('Acertou')
    print ('O numero Randomico {} não é igual ao que tu digitou {}'.format(numero1, numero2))
else:
    print('Errou')
    print('O numero Randomico {} não é igual ao que tu digitou {}'.format(numero1, numero2))
