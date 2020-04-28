def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade > 65:
        return f'Voto opcional com {idade}'
    elif idade < 65 > 18:
        return f'Voto Obrigatório com {idade}'
    else:
        return 'Voto opcional'

nasc = int(input('Digite ano de nascimento: '))
print(voto(nasc))
