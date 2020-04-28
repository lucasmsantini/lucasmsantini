listagem = ('produto1', 1.00,
            'produto2', 2.00,
            'produto3', 3.50,
            'produto4', 4.98,
            'produto5', 5.30,
            'produto6', 6.66,
            'produto7', 7.47)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
