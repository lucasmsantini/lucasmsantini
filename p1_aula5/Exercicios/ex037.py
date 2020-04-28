numero = int(input('Digite um número: '))
print('Opções de conversão:')
print('1 - bytes:')
print('2 - float')
print('3 - str')
print('4 - octal')
print('5 - hex')
print('6 - bin')
op = input("Digite uma das opções acima: ")
if op == '1':
    bytes = bytes(numero)[2:]
    print('Decimal: {}'.format(bytes))
elif op == '2':
    float = float(numero)[2:]
    print('Decimal: {}'.format(float))
elif op =='3':
    str = str(numero)[2:]
    print('Decimal: {}'.format(str))
elif op == '4':
    octal = oct(numero)[2:]
    print('Decimal: {}'.format(octal))
elif op =='5':
    hex = hex(numero)[2:]
    print('Decimal: {}'.format(hex))
elif op =='6':
    bin = bin(numero)[2:]
    print('Binário: {}'.format(bin))
