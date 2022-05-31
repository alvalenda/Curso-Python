# EXERCÍCIO 70: Programa que leia nome e preço de vários produtos. O programa deverá perguntar se o usuário vai
#               continuar. No final mostre: (A) Qual é o total gasto na compra. (B) Quantos produtos custam mais
#               de R$1,000.00   (C) Qual é o nome do produto mais barato.
from time import sleep
print('#' * 20 + ' LOJAS DO POVO ' + '#' * 20)
total = count_1000 = preco_barato = 0
nome_barato = str('')
while True:
    while True:
        try:
            nome = str(input('Produto: ')).strip().title()
        except ValueError:
            print('entrada inválida...')
        else:
            if len(nome) > 0:
                break
            else:
                print('vazio... entrada inválida...')
    while True:
        try:
            preco = abs(float(input('Preço do Produto: R$ ')))
        except ValueError:
            print('entrada inválida...')
        else:
            if len(nome_barato) == 0:
                nome_barato = nome
                preco_barato = preco
            break
    total += preco
    if preco > 1000:
        count_1000 += 1
    if preco < preco_barato:
        preco_barato = preco
        nome_barato = nome
    sleep(0.3)
    print('*=*' * 15 + '\n\t\t\t\tCADASTRADO\n' + '*=*' * 15)
    sleep(0.3)
    while True:
        try:
            menu = str(input('Deseja continuar [S][N]? ')).strip().upper()
        except ValueError:
            print('entrada inválida...')
        else:
            if menu.isalnum():
                if menu[0] in 'SN':
                    menu = menu[0]
                    break
                else:
                    print('entrada inválida...')
            else:
                print('vazio... entrada inválida...')
    if menu[0] in 'Nn':
        print('*=*' * 15)
        print('\t\t\tFINALIZANDO COMPRA')
        sleep(0.5)
        print('*=*' * 15)
        break
    else:
        print('*=*' * 15 + '\n\t\t\t\tNOVO PRODUTO\n' + '*=*' * 15)
        sleep(0.3)
print(f'Valor Total da compra R$:\t{total:,.2f}')
sleep(0.3)
print(f'Produtos acima de R$1.000:\t{count_1000}')
sleep(0.3)
print(f'Produto mais barato:\t\t{nome_barato}')
sleep(0.3)
print('*=*' * 15)
print('FIM')
