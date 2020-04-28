#FÓRMULA: an = a1 + (n - 1) * r
#a1 == primeiro termo
#r == razão
#n == número de termos
#an == termo geral
#sn == soma dos termos

print('Progressão')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = p + (10 - 1) * r
s = 0
for c in range(p,dec + r, r):
    #s = c * p
    #print('{} x {} = {}'.format(p, c, s))
    print(c)