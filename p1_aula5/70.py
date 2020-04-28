continuar = 's'
preco_c = total = cont = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Valor: '))
    continuar = str(input('Deseja continuar? '))
    total += preco
    cont += 1
    if preco > 1000:
        preco_c += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    if continuar == 'n':
        break
print(f'Total da compra: {total}')
print(f'{preco_c} produts custaram mais de mil reais')
print(f'O menor preço foi: {menor}')
