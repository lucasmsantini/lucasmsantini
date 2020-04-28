casa = float(input('Valor da casa: R$ '))
sal = float(input('Salário do satanás: R$ '))
anos = int(input('Quantos anos para pagar? '))
prest = casa / (anos * 12)
trinta = sal * 0.3
if prest > trinta:
    print('Não autorizado. A prest. de \033[35m{:2f}\033[m excede 30% do salário {:.2f}'.format(prest, trinta))
else:
    print('Empréstimo autorizado')
