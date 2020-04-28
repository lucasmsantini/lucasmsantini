dist = float(input('Distância: '))
# dias = int(input('Dias consumidos: '))
if dist > 200:
    vkm = dist * 0.45
else:
    vkm = dist * 0.50
print('O custo da passagem para {} km será de {:.2f} Reais'.format(dist, vkm))
