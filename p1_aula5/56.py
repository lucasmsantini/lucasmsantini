somaidade = 0
media: int = 0
nomevelho = ''
totmulher = 0
for c in range(1,5):
    print('----{}ª pessoa---------------------'.format(c))
    nome = str(input('Digie o Nome: '))
    idade = int(input('Digie a idade: '))
    sexo = str(input('Digie o sexo: [m/f] ')).upper()
    somaidade += idade
    media += somaidade / 4
    if c == 1 and sexo in 'mM':
        maior = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totmulher += 1
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
print('O mais velho tem {} anos e chama-se {}'.format(maior, nomevelho))
print('A média de idade é: {}'.format(media))
