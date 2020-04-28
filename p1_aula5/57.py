sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0] # '[0]' pega a primeira letra somente
while sexo not in 'MmFf':
    sexo = str(input('Valor incorreto. Digie [M] ou [F].')).strip().upper()[0]
print('Fim, pois vc digitou [M/F]')