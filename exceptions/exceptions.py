import winsound

try:
    a = open('arquivo.txt', 'r')
except:
    print('Erro')
    a = open('arquivo.txt', 'w')
    a.write('Deu erro')
finally:
    a.close()

winsound.Beep(300, 1000)
print('next')
winsound.Beep(1300, 1000)
print('next')
winsound.Beep(2300, 1000)
print('next')
winsound.Beep(4300, 1000)
print('next')
winsound.Beep(9000, 2000)