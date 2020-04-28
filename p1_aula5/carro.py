dias = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
tot = (dias * 60) + (km * 0.15)
print(""'Total a pagar é de {:.2f}'"".format(tot))
