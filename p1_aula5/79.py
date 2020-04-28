lista = []
while True:
    num = input('Digite um valor: ')
    if num not in lista:
        lista.append(num)
        print(lista, ' --> adicionado')
    else:
        print(lista, ' --> Duplicado, não adicionado')
    r = str(input('Deseja continuar? [s/n]'))
    if r == 'n':
        break
print(lista,' --> lista original')
lista.reverse()
print(lista,' --> lista em ordem reversa')
lista.sort()
print(lista,' --> lista em ordem crescente')
