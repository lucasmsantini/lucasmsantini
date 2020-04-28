valor = float(input('Qual o valor do produto?: '))
desc = valor - (valor * 0.05)
print('O produto com valor R$ {:.2f}, agora sairá com 5% de desconto, R$ {:.2f} reais'.format(valor, desc))
