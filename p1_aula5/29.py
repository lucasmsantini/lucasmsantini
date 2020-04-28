v = float(input('Qual a velocidade registrada? '))
if v > 80:
    multa = ((v - 80) * 7)
    print ('Multado em {} Reais por estar a {} km/h: '.format(multa,v))
print('Não foi multado')