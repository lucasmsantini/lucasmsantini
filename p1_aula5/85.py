num = [[],[]]
valor = 0
for c in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('¬¬' *60)
print(f'Todos os valores: {num}')
print(f'Pares: {num[0]}')
print(f'Ímpres: {num[1]}')