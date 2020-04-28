from teste import moeda
try:
    valor = float(input('Digite numero: '))

except Exception as erro: # " é o nome da classe, "erro" é uma variável
    print(f'Deu ruim {erro.__cause__}{erro.__class__}')
else:
    print(f'O dobro de {valor} é {moeda.dobro(valor)}')
    print(f'A metade de {valor} é {moeda.metade(valor)}')
    print(f'Aumentar 10% de {valor} dá: {moeda.aumentar(valor, 10)}') #10%
    print(f'Diminuir 10% de {valor} dá: {moeda.diminuir(valor, 10)}')

finally:
    print('volte sempre. ')