n = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            print(c, end=' ')
            n += c
            cont = cont + 1
print('T'*20)
print('Total:',n)
print('Foram encontrados {} números'.format(cont))
