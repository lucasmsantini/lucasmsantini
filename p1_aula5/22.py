nome= input ('Digite teu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '').strip()))
print(len(nome.strip()) - nome.count(' '))
separa = (nome.split())
print (len((separa[0])))