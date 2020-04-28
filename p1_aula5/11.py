tintatem = float(input('Quantos litros de tinta tu tem? '))
custoTinta = float(input('Qual o valor da tinta? '))
alt = float(input('Quanto de altura tem a parede? '))
lar = float(input('Quanto de largura tem a parede? '))
area = alt * lar
tintaprecisa = area / 2
tintautilizavel = tintatem * 2
tintafalta = tintaprecisa - tintautilizavel
custo = tintafalta * custoTinta

print('Você tem {} litros de tinta, sua parede tem {:.2f}m². Sua tinta dá pra pintar {:.2f}m², faltam {:.2f} litros, com o custo de R${:.2f} Reais'.format(tintatem, area, tintautilizavel, tintafalta, custo))