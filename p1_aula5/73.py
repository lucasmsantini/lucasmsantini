times = ('flamengo', 'santos', 'palmeiras', 'gremio', 'atléticoPR',
         'sãoPaulo', 'internacional', 'corinthians', 'fortalezaCE',
         'oiás', 'bahia', 'vasco', 'atléticoMG', 'fluminense', 'botafogo',
         'ceará', 'cruzeiro', 'csa', 'chapecoense', 'avaí')

print('Digite a opção e pressione [ENTER]:')
print('[1] Para mostrar os 5 primeiros ')
print('[2] Para mostrar os 4 lanternas ')
print('[3] Para mostrar em ordem alfabética ')
print('[4] Para mostrar a posição do Chapecoense ')
op = int(input('Escolha: '))

# while 1 >= op >= 4:
if op == 1:
    print(times[:5])
if op == 2:
    print(times[-4:])
if op == 3:
    print(sorted(times))
if op == 4:
    print(f'A chape está na {times.index("chapecoense")}ª posição')
    index = times.index('chapecoense')
    print(f'A posição da chape é: {index}')

