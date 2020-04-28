resp = 's'
soma = qtde = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtde += 1
    if qtde == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Deseja continuar? [s/n] ')[0])
media = soma / qtde
print('Você digitou {} números, e a média foi: {}'.format(qtde, media))
print('O maior número é {}, e o menor: {}'.format(maior, menor))
print('Fim')
