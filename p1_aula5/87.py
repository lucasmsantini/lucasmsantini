matriz = [[0,0,0], [0,0,0], [0,0,0]]
#matriz = [[0]*3]*3
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l} e {c}]'))

print('!!!'*20)
print(matriz)
print('!!!'*20)
for l in range(0,3):
    for c in range(0,3):
        print (f'[{matriz [l][c]}] ', end='')
        if matriz[l][c] % 2 == 1:
            spar += matriz[l][c]
    print()
print('!!!' * 20)
print(f'A soma dos valores pares é: {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da última coluna é: {scol}')
