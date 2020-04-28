km = float(input('Quantos km foram rodados? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
vkm = km * 0.15
vdias = 60 * dias
total = vkm + vdias
print('Você deve ao total \033[32mR$ {:.2f}\033[m por ter rodado {} km em {} dias ao custo de {} por dia.'.format(total, km, dias, vdias/dias))
