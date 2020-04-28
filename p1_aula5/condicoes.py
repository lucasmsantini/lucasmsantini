carro = int(input(('Qual é o ano do seu carro? ')))
if carro >= 12:
    print('Carro Velho, pois tem {} ano'.format(carro))
else:
    print ('Carro novo, pois tem menos que {} anos'.format(carro))
