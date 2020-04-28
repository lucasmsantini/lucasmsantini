def leiaInt(msg):
    ok = False
    valor = 0
    try:
        while True:
            n = str(input(msg))
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print('\033[0;31mERRO, valor inválido.\033[m')
            if ok:
                break
    except Exception as erro:
        print(f'Causa do erro: {erro.__class__}')
    return valor

def leiaFloat(msg):
    ok = False
    valor = 0
    try:
        while True:
            n1 = str(input(msg))
            if n1.isalnum():
                valor = float(n1)
                ok = True
            else:
                print('\033[0;31mERRO, valor inválido.\033[m')
            if ok:
                break
    except Exception as erro:
        print(f'Causa do erro: {erro.__class__}')
    return valor


n = leiaInt('Digite um número inteiro: ')
n1 = leiaFloat('Digite um número Real: ')
print(f'Você digitou o numero inteiro: {n}')
print(f'Você digitou o numero Real: {n1}')