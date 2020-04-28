a = float(input('Digite a altura: '))
b = float(input('Digite a largura: '))
area = a * b
tinta = area * 2
print('A área da parede a ser pintada é de \033[0:30:42m  {}  \033[m m²'.format(area))
print('Para pintar sua parede, vai precisar de {:.2f} litros de tinta'.format(tinta))
