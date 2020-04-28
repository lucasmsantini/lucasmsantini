from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
dados['ctps'] = int(input('CTPS: '))
nasc = int(input('Ano Nascimento: '))
dados['idade'] = datetime.now().year - nasc
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano Contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
    print('!!'*30)
    for k, v in dados.items():
        print(f'{k}: {v}')
else:
    print(dados)