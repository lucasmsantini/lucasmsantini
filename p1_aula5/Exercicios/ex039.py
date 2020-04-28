from datetime import date

ano = date.today().year
print('Estamos em: ', ano)
idade = int(input('Digite sua idade: '))
nasc = ano - idade
print('Nasceu em: ', nasc)
if idade == 19:
    calc = idade - 18
    print('Passou 1 ano da idade de se alistar')
elif idade == 666:
    print('Satanás')
elif idade > 18:
    calc = idade - 18
    print('Passou {} anos da idade de se alistar'.format(calc))
elif idade == 18:
    print('Aliste-se este ano.')
else:
    calc = 18 - idade
    print('Faltam {} anos para vc se alistar'.format(calc))
