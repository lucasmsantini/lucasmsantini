valor = float(input('Digite o valor: '))
print('Opções: 1- Dinheiro/Cheque')
print('Opções: 2- cartão')
print('Opções: 3- 2x Cartão')
print('Opções: 4- 3x ou maios')
cond = int(input('Opção: '))
if cond == 1:
    desc = valor * 0.10
    tot = valor - desc
    print('Desconto de {:.2f}. Total a pagar: {:.2f}'.format(desc, tot))
elif cond == 2:
    desc = valor * 0.05
    tot = valor - desc
    print('Desconto de {:.2f}. Total a pagar: {:.2f}'.format(desc, tot))
elif cond == 3:
    print('Sem desconto. Total a pagar: {:.2f}'.format(valor))
elif cond == 4:
    jur = valor * 0.2
    tot = valor + jur
    print('Juros de {:.2f}. Total a pagar: {:.2f}'.format(jur, tot))
else:
    print('Digite uma das opções acima.')