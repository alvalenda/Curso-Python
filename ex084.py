# EXERCÍCIO 84: Programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
#               [A] Quantas pessoas foram cadastradas       [B] Uma listagem com as pessoas mais pesadas
#               [C] Uma listagem com as pessoas mais leves
pessoa = list()
grupo = list()
gordo = list()
magro = list()
count = maior = menor = int(0)
print(f'=*' * 25)
while True:
    while True:
        nome = str(input(f'{count + 1}º NOME: ')).strip().title()
        if bool(nome):
            pessoa.append(nome)
            break
        else:
            print(f'vazio... tente novamente')
    while True:
        try:
            peso = float(input(f'{count + 1}º PESO: '))
        except ValueError:
            print(f'inválido... tente novamente')
        else:
            peso = abs(peso)
            pessoa.append(peso)
            if count == 0:
                maior = menor = peso
            elif peso > maior:
                maior = peso
            elif peso < menor:
                menor = peso
            count += 1
            break
    grupo.append(pessoa[:])
    print(f'=*' * 25)
    while True:
        menu = input(f'Deseja adicionar mais pessoas: ').strip().upper()
        if bool(menu):
            menu = menu[0]
            if menu in 'SN':
                break
            else:
                print(f'entrada inválida, tente [S] ou [N]')
        else:
            print(f'vazio...')
    print(f'=*' * 25)
    pessoa.clear()
    if menu in 'N':
        break
for i in grupo:
    if i[1] == maior:
        gordo.append(i[0])
    if i[1] == menor:
        magro.append(i[0])
print(f'Foram cadastradas um total de {count} pessoas')
print(f'Pessoas mais forrrrrtes com {maior:.2f} Kg:', end=' ')
for i in gordo:
    print(f'{i}', end=', ')
print(f'\nPessoas mais magraxxx com {menor:.2f} Kg:', end=' ')
for i in magro:
    print(f'{i}', end=', ')
print(f'\nFIM!!!')
