sal = float(input('Qual seu salário? '))
if sal <= 1250:
    novosal = (sal * 0.15) + sal
    print('seu salário foi de {:.2f} para {:.2f}'.format(sal, novosal))
else:
    novosal = (sal * 0.1) + sal
    print('seu salário foi de {:.2f} para {:.2f}'.format(sal, novosal))
