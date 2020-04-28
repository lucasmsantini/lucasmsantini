print('========== Tabuada =========')
while True:
    num = float(input('Digite um número (negativo para parar): '))
    if num < 0:
        break
    for cont in range(1,11):
        print (f'{num:.0f} x {cont} = {num * cont:.0f}')
print('Fim')