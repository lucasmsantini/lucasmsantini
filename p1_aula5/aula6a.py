n1 = float(input('digite numero: '))
n2 = int(input('digite outro: '))
n3 = int(input('digite mais um: '))
n0 = input('digite algo: ')
soma = n1 + n2
menos = n1 - n2
divi = n1 / n2
mult = n1 * n2
pot = n1 ** n2
inte = n1 // n2
rest = n1 % n2
print('----------------------     Operações    -----------------------')
print('O antecessor de {} é {}'.format(n1, (n1-1)))
print('O sucessor de {} é {}'.format(n1, (n1+1)))
print('A soma entre os números {} e {} é: {} e a diferença é {} e a multiplicação dá {} e a divisão é {} e a potência '
      'é {}'.format(n1, n2, soma, menos, divi, mult, pot))
print('O dobro de {} é {}'.format(n1, (n1*2)))
print('O triplo de {} é {}'.format(n1, (n1*3)))
print('A raiz quadrada de {} é {}'.format(n1, (n1**(1/2))))
print('A divisão inteira entre os números {} e {} é: {}'.format(n1, n2, inte))
print('O resto da divisão entre os números {} e {} é: {}'.format(n1, n2, rest))
print('---------------------- Tipos Primitivos -----------------------')
print('E a última coisa que tu digitou foi: {}'.format(n0))
print('  |---- é numérico? {}, é alfa? {}, é decimal? {}, é upper? {}, é alfanumérico? {}'.format(n0.isnumeric(),
                                                                                                  n0.isalpha(),
                                                                                                  n0.isdecimal(),
                                                                                                  n0.isupper(),
                                                                                                  n0.isalnum()))
