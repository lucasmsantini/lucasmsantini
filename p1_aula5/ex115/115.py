from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('\033[0;35mArquivo de dados OK\033[m')
else:
    print('\033[0;31m---> Arquivo de dados não encontrado <---\033[m')
    criarArquivo(arq)
# if not arquivoExiste(arq):
#     criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
        print('Teste opção 1')
    elif resposta == 2:
        nome = str(input('Digite o nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        print('Teste opção 2')
    elif resposta == 3:
        print('Saindo do programa')
        break
    else:
        print('Erro, opção inválida')
    sleep(2)
