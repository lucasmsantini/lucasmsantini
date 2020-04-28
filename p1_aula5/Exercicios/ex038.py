a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
if a > b:
    print('O número {} é maior que o {}'.format(a,b))
elif a == b:
    print('Os números {} e {} são iguais'.format(a,b))
else:
    print('O número {} é maior que {}'.format(b,a))
