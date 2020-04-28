lanche = 'Hamburguer', 'pizza', 'pudim', 'suco', 'batata'
lanche = 'Hamburguer', 'pizza', 'pudim', 'suco', 'batata'
print(lanche)  # ('Hamburguer', 'pizza', 'pudim')
print(lanche[1])  # pizza
print(lanche[0])  # hamburguer
print(lanche[2:])  # ('pudim', 'suco', 'batata')
print(lanche[1:3])  # ('pizza', 'pudim')
print(lanche[:2])  # ('Hamburguer', 'pizza')
print(lanche[-1])  # batata
print(lanche[-1:])  # ('batata',)
print(lanche[-2])  # suco
print(lanche[-4:])  # ('pizza', 'pudim', 'suco', 'batata')

print('-' * 20)
print(lanche)
print(sorted(lanche))  # em ordem alfabetica

print('-' * 20)
for cadacomida in lanche:
    print(f'Eu vou comer {cadacomida}')
print('------ Encheu a pança')

print('-' * 20)
for pos, cadacomida in enumerate(lanche):
    print(f'Eu vou comer {cadacomida} na posição {lanche}')
print('------ Encheu a pança')

print('-' * 20)
print('Temos:', len(lanche), 'lanches ao total')

print('-' * 20)
for contador in range(0, len(lanche)):
    print(f'Eu vou comer', lanche[contador])

print('-' * 20)
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')

print('-' * 20)
a = (7, 2, 4, 6)
b = (1, 3, 5, 7)
c = a + b
print(a)
print(b)
print(c)
print(sorted(c))
print(c.count(5))  # Mostra quantas vezes o %5% aparece
print(len(c))
print(c.index(3))  # posição do elemento, procurando o "3"
print(c.index(7))
print(c.index(7, 1))  # DESLOCAMENTO   -   ", 1" faz o indexador ignorar a primeira posição

print('-' * 20)
print('Del')
pessoa = ('lucas', 37, 'M', 99.99)
del pessoa

print('-' * 20)
print(pessoa)
pessoa = ('lucas', 37, 'M', 99.99)
print(pessoa)
