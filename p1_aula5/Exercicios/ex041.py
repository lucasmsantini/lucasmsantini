from datetime import date

nasc = int(input('Ano de Nascimento: '))
ano = date.today().year
print('Estamos no ano de: {}'.format(ano))
idade = ano - nasc
print('Você tem {} anos de idade, conforme nossos registros, você se encaixa na modalidade: '.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade >= 14:
    print('INFANTIL')
elif idade >= 19:
    print('JUNIOR')
elif idade >= 20:
    print('SENIOR')
else:
    print('MASTER')
