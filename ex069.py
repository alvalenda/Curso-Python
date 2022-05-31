# EXERCÍCIO 69: Programa que leia a idade e o gênero de várias pessoas. A cada pessoa cadastrada o programa deverá
#               perguntar se o usuário quer ou não continuar. No final, mostre: (A) quantas pessoas tem mais de 18 anos
#               (B) quantos homens foram cadastrados. (C) quantas mulheres tem menos de 20 anos.
from time import sleep
print('Cadastro do Banco de Dados YYZ')
count_maior18 = count_mulher20 = count_homem = 0
while True:
    while True:
        try:
            idade = abs(int(input('Idade: ')))
        except ValueError:
            print('entrada inválida...')
        else:
            break
    while True:
        try:
            genero = str(input('Gênero [M][F]: ')).strip().upper()
        except ValueError:
            print('entrada inválida...')
        else:
            if genero.isalnum():
                if genero[0] in 'MF':
                    genero = genero[0]
                    break
                else:
                    print('entrada inválida...')
            else:
                print('vazio... entrada inválida...')
    if idade >= 18:
        count_maior18 += 1
    if genero in 'M':
        count_homem += 1
    if genero in 'F' and idade < 20:
        count_mulher20 += 1
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
        print('Encerrando...')
        sleep(0.5)
        print('*=*' * 20)
        break
    else:
        print('*=*' * 15 + '\n\t\t\t\tNOVO CADASTRADO\n' + '*=*' * 15)
        sleep(0.3)
print(f'Maiore(s): {count_maior18}')
sleep(0.3)
print(f'Boludo(s): {count_homem}')
sleep(0.3)
print(f'Novinha(s): {count_mulher20}')
sleep(0.3)
print('FIM')
