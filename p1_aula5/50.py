cont = 0
s = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        cont += 1
        s += n
print('nº pares: {}, soma: {}'.format(cont, s))
