n = []
par = []
imp = list()
while True:
    n.append(int(input('Digite um numero: ')))
    r = str(input('Deseja continuar? [s/n]'))
    if r == 'n':
        break
print('&&' * 30)
print('Lista completa:  ', n)
print(f'Você digitou: {len(n)} números, destes, ', end='')
for i, n in enumerate(n):
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        imp.append(n)
print(f'{par} são pares ', end='')
print(f'e {imp} são ímpares')
