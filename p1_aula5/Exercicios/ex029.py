vel = int(input('Qual a velocidade do carro/ '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Multado em R$ {:.2f} Reais'.format(multa))
else:
    print('Siga em frente, olhe para o lado')