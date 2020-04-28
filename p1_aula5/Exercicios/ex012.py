sal = float(input("Salário: "))
novosal = sal + (sal * 0.15)
print('O novo salário que era de {} reais agora foi para \033[2:31:40m {:.2f} \033[m reais com os 15% de aumento.'.format(sal, novosal))
