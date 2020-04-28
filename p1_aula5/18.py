from math import sin, cos, tan, radians

a = float(input('digite um ângulo: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('Seno: {:.2f}, cosseno {:.2f}, tangente {:.2f}'.format(seno, cos, tan))