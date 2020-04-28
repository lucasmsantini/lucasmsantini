valor = int(input('Quanto é a coisa? '))
desconto = int(input('Quantos % de desconto? '))
desc = desconto / 100
soma = valor - (valor * desc)
economia = valor - soma
print ('Seu produto custa {} Reais e com {}% de desconto, fica por {} Reais. Você economizou {:.2f} Reais'.format(valor, desconto, soma, economia))