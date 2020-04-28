from random import choice
nome1 = input('n1: ')
nome2 = input('n2: ')
nome3 = input('n3: ')
nome4 = input('n4: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O escolhido foi: {}'.format(escolhido))