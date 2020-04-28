aluno = {} # ou dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['sitoacao'] = 'Aprovado'
elif 5 <= aluno['media'] <7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(aluno.values())
print(aluno.keys())
print(aluno.items())
print()
print()
print()
for k, v in aluno.items():
    print(f'{k}: {v}')