n = []
while True:
    n.append(int(input('Digite um numero: ')))
    r = str(input('Deseja continuar? [s/n]'))
    if r == 'n':
        break
print('&&'*30)
n.sort(reverse=True)
print(n)
if 5 in n:
    print('O 5 está na lista')
else:
    print('O 5 Não está na lista')
print(f'Você digitou: {len(n)} números')