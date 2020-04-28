pessoa = {
    'primeiro_nome': 'lucas',
    'ultimo_nome':'santini',
    'idade':'38'
    }

pessoa = dict(primeiro_nome='teste', ultimo_nome='sobrenome') # outro método de incluir dados
print(pessoa, type(pessoa))

#get values
print(pessoa['primeiro_nome'])
print(pessoa.get('ultimo_nome'))

#adicionar valores
pessoa['fone'] = 442234224

print(pessoa.items())

pessoa2 = pessoa.copy()
pessoa2['cidade'] = 'Lages'
print(pessoa2)
pessoa2.pop('fone')
print(pessoa2)