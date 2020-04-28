def line():
    print('-=' * 35)


def mensagem(msg):
    print(msg)
    line()


line()
mensagem('Teste python')
mensagem('Lucas Santini')
mensagem('NDDigital')


def soma1(a, b):
    s = a + b
    print('Resultado da soma:', s)


soma1(5, 5)
soma1(a=3, b=2)
soma1(b=3, a=2)
line()


def soma(a, b):
    s = a + b
    print(s)


def contador(*num):
    print(num)


contador(2, 5, 4)
contador(5, 2, 1, 4, 1)
contador(52, 2)
 