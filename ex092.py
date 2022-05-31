# EXERCÍCIO 92: Programa leia NOME, ANO de NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com a idade) em um
#               dicionário, se por acaso o CTPS for diferente de ZERO, o dicionário receberá também receberá
#               o ano de contratação e o salário. Calcule e acrescente, com quantos anos a passoa vai se aposentar.
#               35 anos de variação
from datetime import datetime
from time import sleep
ano_atual = datetime.now().year
pessoa = dict()
lista = list()
while True:
    print(f'='*50 + f'\n{"NOVO CADASTRO":^50}' + f'\n' + f'='*50)
    while True:
        nome = str(input(f'Nome: ')).strip().title()
        if bool(nome):
            break
    while True:
        try:
            ano_nasc = int(input(f'Ano de Nascimento: '))
        except ValueError:
            print(f'...')
        else:
            break
    while True:
        try:
            ctps = int(input(f'Número CTPS: '))
        except ValueError:
            print(f'...')
        else:
            break
    pessoa['Nome'] = nome[:30]
    pessoa['Idade'] = (ano_atual - abs(ano_nasc))
    pessoa['CTPS'] = abs(ctps)
    if ctps > 0:
        while True:
            try:
                ano_cont = int(input(f'Ano de Contratação: '))
            except ValueError:
                print(f'...')
            else:
                break
        while True:
            try:
                salario = float(input(f'Salário R$: '))
            except ValueError:
                print(f'...')
            else:
                break
        pessoa['Contratado'] = abs(ano_cont)
        pessoa['Salário'] = abs(salario)
        pessoa['Aposentadoria'] = (ano_cont + 35)
    lista.append(pessoa.copy())
    pessoa.clear()
    print(f'=' * 50)
    while True:
        menu = str(input(f'Novo cadastro? ')).strip().upper()
        if bool(menu):
            menu = menu[0]
            if menu in 'SN':
                break
    if menu in 'N':
        print(f'=' * 50)
        break
for i in lista:
    for k, v in i.items():
        if k in 'Salário':
            print(f'{k:<13}:\tR$ {v:,.2f}')
        else:
            print(f'{k:<13}:\t{v}')
    sleep(1)
    print()
print(f'FIM!!!')
