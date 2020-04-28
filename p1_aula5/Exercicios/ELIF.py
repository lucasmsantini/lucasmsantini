nome = str(input('Digite seu nome: '))
if len(nome) > 5:
    print('{}, seu nome possui {} caracteres, mais que 5'.format(nome, len(nome)))
elif nome == 'lucas':
    print('O nome {} é o mais bonito de todos'.format(nome))
elif nome in 'ana claudia jessica duda jana':
    print('Nome errado')
else:
    print('Nome else')
