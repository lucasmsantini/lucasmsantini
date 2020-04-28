from datetime import date
tmaior = 0
tmenor = 0
atual = date.today().year
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        tmaior += 1
    else:
        tmenor += 1
print('Total de pessoas maiores: {}'.format(tmaior))
print('Total de pessoas menores: {}'.format(tmenor))