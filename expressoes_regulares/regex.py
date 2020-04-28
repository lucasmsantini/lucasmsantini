import re

string_teste = 'o rato roeu a roupa do rei de roma'

# padrao = re.search(r'rato', string_teste)
padrao = re.search(r'rat.', string_teste)
# padrao = re.search(r'rat\w', string_teste)
# padrao = re.search(r'ra\w\w', string_teste)
padrao_f = re.findall(r'ro\w*', string_teste)

if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')

if padrao_f:
    print(padrao_f)
else:
    print('Padrão não encontrado')