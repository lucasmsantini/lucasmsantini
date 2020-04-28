tot = 0
numero = int(input('Digite um numero inteiro: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('{}'.format(c), end=' ')
    tot += 1
print('Total: ',tot)
if tot == 2:
    print('Número primo')
else:
    print('Não é primo')