lanches = ['hamburguer', 'suco', 'pizza', 'pudim', 'sorvete']
lanches[2] = 'teste'
print(lanches)
print('*' * 50)
lanches.append('adicionado por ultimo')
print(lanches)
print('*' * 50)
lanches.insert(1, 'Cachorro quente na posição 1')
print(lanches)
print('*' * 50)
del lanches[5]  # elimina um lanche pelo índice
print(lanches)
print('*' * 50)
lanches.pop(3)  # elimina o último, porém podemos usar o índice para indicar
print(lanches)
print('*' * 50)
lanches.remove('suco')  # remove pelo conteúdo, e não pelo índice
print(lanches)
print('*' * 50)
if 'pudim' in lanches:
    lanches.remove('pudim')
print(lanches)
print('*' * 50)
valores = list(range(4, 11))
print(valores)
print('*' * 50)
valores = [8, 2, 5, 4, 2, 3, 5, 6, 7]
print(sorted(valores))
print('*' * 50)
tamanho = len(valores)
print(f'A lista tem {tamanho}, elementos')
print('*' * 50)
valores.sort(reverse=True)
print(valores)
print('*' * 50)
if 2 in valores:
    valores.remove(2)
print(valores)
print('*' * 50)
valores = []
valores.append(3)
valores.append(6)
valores.append(3)
for valor in valores:
    print(f'{valor} .. ')
print('*' * 50)
for i, valor in enumerate(valores):  # -----> indice, valor
    print(f'Na posição {i} encontrei o valor {valor} .. ')
print('*' * 50)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    for i, valor in enumerate(valores):  # -----> indice, valor
        print(f'Na posição {i} encontrei o valor {valor} .. ')
print('*' * 50)
a = [2,3,2,8,4]
b = a[:] #  Copia a lista, sem fazer uma ligação entre elas [:][:][:]
print(a)
print(b)