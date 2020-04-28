for c in range(1,11,):
    print(c, end=' ')
print('Fim for')

c = 0
while c < 10:
    c += 1
    print(c, end=' ')
print('Fim while')

v = 0
teste = 0
continua = 's'
par = impar = 0
while continua == 's':
    valor = int(input('Digite valor: '))
    v += 1
    teste = valor + teste
    continua = str(input('continuar? [s/n] '))
    if valor % 2:
        par += 1
    else:
        impar += 1
print('Quantidade de repetições {}'.format(v))
print('Quantidade de nº pares: {}'.format(par))
print('Quantidade de ímpares: {}'.format(impar))
print('Soma dos valores: {}'.format(teste))
print('Fim')