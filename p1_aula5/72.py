cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número de ZERO a VINTE: '))
while 0 >= num >= 20:
    num = int(input('Digite um número de ZERO a VINTE: '))
    print(cont[num])
print('Fim')