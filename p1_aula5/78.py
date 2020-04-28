print('88'*20)
num = []
for cont in (range(0,5)):
    num.append(int(input(f'Digite um numero para a posição {cont}: '))) # cont--> indice
    for i, valor in enumerate(num):
        print('nummm ', num)
        print('iiiiii ', i)
        print(f'O numero: {num} está na posição {i}')
print('Os números digitados foram: ', num)
print ('maior: ', max(num))
print ('menor: ', min(num))