a = float(input('Digite o angulo A: '))
b = float(input('Digite o angulo B: '))
c = float(input('Digite o angulo C: '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Os ângulos {}, {} e {} formam um triÂngulo'.format(a, b, c))
else:
    print('Os ângulos {}, {} e {} NÃO formam um triângulo'.format(a, b, c))
