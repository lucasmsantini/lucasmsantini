frase = ('Curso em Vídeo Python')
frase1 = ('            Curso em Vídeo Python  ')
print(frase[0:1])
print(frase[1])
print(frase[13:])
print(frase.count('0'))
print(frase.count('o', 0, 13))
print(frase.upper().count('O'))
print(frase.upper())
print(frase1.strip())
print(frase1.rstrip())
print(frase.replace('Python', 'Android'))
print(len(frase))
print(frase[0])
print('Curso' in frase)
print(frase.find('teste'))
print(frase.split())
print(frase.lower().find('video'))
dividido = frase.split()
print (dividido[0])
dividido = frase.split()
print (dividido[2][3])