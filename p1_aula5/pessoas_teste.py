pessoas_teste = [['pedro', 25], ['maria', 18], ['joão', 30], ['moisés', 20], ['catarina', 23]]
print(pessoas_teste, end=' '), print(pessoas_teste[0], end=' '), print(pessoas_teste[0][1], end=' '), print(pessoas_teste[1][1])
print('##' * 20)

for unidade in pessoas_teste:
    print(f'{unidade[0]} tem {unidade[1]} anos de idade.', end=' ')

print('##' * 20)
galera = list()
dado = list()
for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  ###################### não esquecer a CÓPIA da lista
    dado.clear()
print(galera)
totma = totme = 0
for p in galera:  # para cada pessoa em galera
    if p[1] >= 18:
        print(p[0], ' é maior')
        totma += 1
    else:
        print(p[0], ' é menor')
        totme += 1
print(f'Total maiores: {totma} e total menores: {totme}')
