print('Progressão')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p
contador = 1
while contador <= 1000:
    termo += r
    contador += 1
    print('{} -'.format(termo), end='')
print('End')