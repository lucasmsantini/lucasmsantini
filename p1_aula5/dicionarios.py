filme = {'título': 'Star Wars',
         'ano': '1977',
         'diretor': 'George Lucas'}
print(filme.items())
print('***' * 20)
for k, v in filme.items():
    print(f'O {k} é {v}')
print('***' * 20)
for k, v in filme.items():
    print(k)
print('***' * 20)
for k, v in filme.items():
    print(v)
print('***' * 20)
print(filme.keys())

print(filme.values())
print(filme.items())
del filme['ano']
print(filme.items())
brasil = []
estado1 = {'uf': 'santacatarina', 'sigla': 'sc'}
estado2 = {'uf': 'rioGrandeDoSul', 'sigla': 'rs'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1]['sigla'])
del brasil

print('***' * 20)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf: '] = str(input('Unidade Federativa: '))
    estado['sigla: '] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  # sempre copiar, para inserir na lista, com o MÉTODO COPY
print(brasil)
for e in brasil:
    print(e)
for l in brasil:
    for k,v in l.items():
        print(f'O campo {k} tem valor {v}')
for i in brasil:
    for v in i.values():
        print(v, end=', ')
    print()