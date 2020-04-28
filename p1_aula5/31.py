distancia = float(input('Qual a distancia percorrida? '))
if distancia > 200:
    valor = (distancia * 0.45)
    print('O Valor para {} km é de R$ {:.2f} reais'. format(distancia, valor))
else:
    valor = (distancia * 0.50)
    print ('O valor para {} km é de R$ {:.2f} reais'.format(distancia, valor))
