# EXERCÍCIO 94: Leia NOME, GENERO e IDADE de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
#               os dicionários em uma lista. No final, mostre:
#               (A) Quantas pessoas foram cadastradas       (B) A média de idade do grupo
#               (C) Uma lista com todas as mulheres         (D) Uma lista c/ todas as pessoas com idade acima da média
pessoa = dict()
lista = list()
lista_mulheres = list()
lista_maduros = list()
conta = conta_idade = int(0)
print(f'='*60 + f'\n{"BANCO DE DADOS DA GALERA":^60}' + f'\n' + f'='*60)
while True:
    print(f'Cadastro da {conta + 1}ª pessoa:')
    while True:
        nome = str(input(f'Nome: ')).strip().title()
        if bool(nome):
            nome = nome[:30]
            break
        else:
            print(f'...')
    while True:
        genero = str(input(f'Gênero: ')).strip().upper()
        if bool(genero):
            genero = genero[0]
            if genero in 'MF':
                break
        else:
            print(f'[M][F]...')
    while True:
        try:
            idade = int(input(f'Idade: '))
        except ValueError:
            print(f'...')
        else:
            conta_idade += abs(idade)
            break
    conta += 1
    pessoa['Nome'] = nome
    pessoa['Genero'] = genero
    pessoa['Idade'] = abs(idade)
    if pessoa['Genero'] in 'F':
        lista_mulheres.append(pessoa.copy())
    lista.append(pessoa.copy())
    pessoa.clear()
    print(f'{" PESSOA CADASTRADA COM SUCESSO ":=^60}')
    while True:
        menu = str(input(f'Adicionar nova pessoa? ')).strip().upper()
        if bool(menu):
            menu = menu[0]
            if menu in 'SN':
                break
    if menu in 'N':
        print(f'{" FINALIZANDO ":=^60}')
        break
    else:
        print(f'=' * 60)
media_idade = float(conta_idade / conta)
for p in lista:
    if p['Idade'] > media_idade:        # testar se idade é maior que a média / Se SIM, colocar na lista de velhos
        lista_maduros.append(p.copy())
# print(f'{lista}')
# (A) QUANTAS PESSOAS FORAM CADASTRADAS
print(f'Foram cadastradas {conta} pessoas.')
# (B) MÉDIA DE IDADE DO GRUPO
print(f'Média de idade do grupo: {media_idade}')

# (C) Uma lista com todas as mulheres
print(f'Mulheres do grupo:\t\t ', end='')
for p in lista_mulheres:
    print(f'[', end='')
    for k, v in p.items():
        if k in 'Idade':
            print(f'{v} anos', end='], ')
        else:
            print(f'{v}', end=', ')
# (D) Uma lista c/ todas as pessoas com idade acima da média
# print(f'{lista_maduros}')
print()
print(f'Acima da média da idade: ', end='')
for p in lista_maduros:
    print(f'[', end='')
    for k, v in p.items():
        if k in 'Idade':
            print(f'{v} anos', end='], ')
        else:
            print(f'{v}', end=', ')
print(f'\nFIM!!!')
