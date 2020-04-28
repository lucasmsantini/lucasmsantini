from random import randint
numeros = (randint (1, 10)), (randint (1, 10)), (randint (1, 10)), (randint (1, 10)), (randint (1, 10))
for n in numeros:
    print(f'{n} ', end='')
print(f'\nMaior: {max(numeros)}')
print(f'Menor: {min(numeros)}')