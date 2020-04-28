def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO, valor inválido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número inteiro: ')
print(f'Você digirou o numero: {n}')