nome = str(input('Digite seu nome completo: '))
lista = nome.split()
print(lista)
print("seu 1º e último nomes são: \033[34m{} {}".format(lista[0],lista[len(lista)-1]))
