temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Continuar? '))
    if resp == 'n':
        break
print(f'Dados digitados: {princ}')
print(f'Total: {len(princ)}')
print(f'Maior peso: {mai}')
print(f'Menor peso: {men}')