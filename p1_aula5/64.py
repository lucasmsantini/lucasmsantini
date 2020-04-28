cont = n = soma = 0
n = int(input('Digite um número: [999 para parar]'))
while n != 999:
    cont += 1
    soma = soma + n
    n = int(input('Digite um número: [999 para parar]'))
print('{} nº foram digitados. Total: {}'.format(cont, soma))