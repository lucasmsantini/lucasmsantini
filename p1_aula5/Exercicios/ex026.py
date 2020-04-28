frase = str(input('Digite uma frase: ')).strip()
print('A letra "a" aparece {} vezes na frase acima.'.format(frase.lower().count('a')))
print('A última letra "a" aparece na posição {}'.format(frase.lower().rfind('a')))
print('A primeira letra "a" aparece na posição {}'.format(frase.lower().find('a')))