
cont = soma = 0
while True:
    num = int(input('Digite um número, ou [999] para sair: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Foram digitados {cont} números, e a soma deles foi {soma}')
print('Fim')
