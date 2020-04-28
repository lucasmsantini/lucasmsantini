n1 = input(('Digite o 1ª valor: '))
n2 = input(('Digite o 2º valor: '))
n3 = input(('Digite o 3º valor: '))
if n1 > n2 and n1 > n3:
    print('{} é o maior'.format(n1))
if n2 > n3 and n2 > n1:
    print('{} é o maior'.format(n2))
else:
    print ('{} é o maior'.format(n3))
if n1 < n2 and n1 < n3:
    print ('{} é o menor'.format(n1))
if n2 < n1 and n2 < n3:
    print ('{} é o menor '.format(n2))
else:
    print ('{} é o menor'.format(n3))
