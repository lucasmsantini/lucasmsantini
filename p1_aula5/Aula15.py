n = s = 0
cont = 0
while cont < 10:
    cont += 1
    print(cont, '-> ', end='')
print('Fim')
cont = 0
valor = int(input('Digite um valor'))
while True:
    cont += 1

    if cont == 666:
        break
    s = cont + valor
print(f'A soma é {s}')
print('Fim---------------------')
nome = str(input('Digite um nome: '))
salario = float(input('Digite o salário: '))
print(f'O nome digitado é: {nome}') # Phyton 3.6+
print('O nome é: {}'.format(nome)) # Phyton 3.6
print('O nome digitado foi %sS' % (nome)) # Phyton 2
print(f'O nome é {nome:^20} e o salário é {salario:.2f}') # ----------------------------