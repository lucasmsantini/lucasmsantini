lista = []  # ou lista = lista()
for cont in (range(0, 5)):
    n = int(input('Digite um valor: '))
    maior = menor = n
    if cont == 0:  # primeiro valor
        lista.append(n)
    elif n > lista[-1]:  # último valor
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
