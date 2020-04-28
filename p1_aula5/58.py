from random import randint
palpites = 0
acertou = False
comp = randint(1, 10)
while not acertou:
    user = int(input('Digite um número de 1 a 10: '))
    palpites += 1
    if comp == user:
        acertou = True
    else:
        if comp > user:
            print('Nº mais alto')
        elif comp < user:
            print('Nº mais baixo')
    if user > 10:
        user = int(input('Digite novamente: '))
print('O Computador escolheu o nº {}, e vc {}'.format(comp, user))
print('Acertou!!! Precisou de {} tentativas'.format(palpites))
