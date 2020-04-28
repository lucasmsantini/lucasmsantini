from math import sin,cos,tan,radians
an = float(input('Digite o valor do ângulo: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('O ângulo informado {} possui um cosseno de {:.2f}, um seno de {:.2f} e uma tangente de {:.2f}.'.format(an,cosseno,seno,tangente))
