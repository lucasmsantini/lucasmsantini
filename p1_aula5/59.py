
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
op = maior = 0
while op != 5:
    print('-' * 20)
    op = int(input('''Menu de opções:
[1] Somar 
[2] Multiplicar 
[3] Maior 
[4] Novos nºs 
[5] Sair d programa '''))
    if op == 1:
        print('Opção ------------ Somar: {} + {} = {}'.format(v1,v2, (v1 + v2)))
    elif op == 2:
        print('Opção ------ Multiplicar: {} x {} = {}'.format(v1,v2, (v1 * v2)))
    elif op == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Opção ------------ Maior: {}'.format(maior))
    elif op == 4:
        print('Opção -------- Novos nºs, digite os novos números: ')
        v1 = int(input('Digite o 1º valor: '))
        v2 = int(input('Digite o 2º valor: '))
    elif op == 5:
        print('Finalizando. Aguarde')
    else:
        print('Opção inválida')
print('Fim do programa')
