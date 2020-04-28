continua = 's'
controle = tot18 = toth = totf = 0
while True:
    sexo = str(input('Sexo [M/F]: '))
    idade = int(input('Digite a idade: '))
    continua = str(input('Desena continuar? [s/n] '))
    if idade >= 18:
        tot18 += 1
    if sexo == 'm':
        toth += 1
    if sexo == 'f' and idade < 20:
        totf += 1
    if continua == 'n':
        break
print(f'Total pessoas com mais de 18: {tot18}')
print(f'Total homens com mais de 18 anos: {toth}')
print(f'Total mulheres com menos de 20 anos: {totf}')
print('Fim')