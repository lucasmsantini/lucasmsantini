nota1 = float(input('Nota: '))
nota2 = float(input('Nota2: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('APROVADO')
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')