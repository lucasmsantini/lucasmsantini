print('Progressão')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p
contador = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -'.format(termo), end='')
        termo += r
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais deseja mostrar? '))
print('Finalizado com {} termos ao total'.format(total))
