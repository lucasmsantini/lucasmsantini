n = input('Digite seu nome completo: ').strip()
nome = n.split()
print('Maiusculas: {}'.format(n.upper()))
print('Minusculas: {}'.format(n.lower()))
print('Quantas letras tem?: {}'.format(len(n) - n.count(' ')))
print(nome)
print('Quantas letras tem o 1º nome: {}'.format(len(nome[0])))
