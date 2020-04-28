from random import randint

tipo = total = 0
while True:
    jogador = int(input('Digite um número:'))
    comp = randint(0, 1)
    tipo = str(input('Par o Ímpar? [P/I] '))
    if tipo == 'P':
        if total % 2 == 0:
            print('você venceu')
        else:
            print('você perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('você perdeu')
        else:
            print('você venceu')
            break
print('Perdeu')