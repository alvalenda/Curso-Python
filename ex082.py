# EXERCÍCIO 82: Programa que vai ler vários números e colocar em uma lista. Depois, crie duas listas extras que vão
#               conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#               ao final, mostre o conteúdo das três listas geradas.
def ler_int():
    global cont
    while True:
        try:
            n = int(input(f'Entre com {cont + 1}º número: '))
        except ValueError:
            print('valor inválido, tenta novamente...')
        else:
            cont += 1
            return n


def imp_lista(p):
    for k in p:
        print(f'{k}', end=' ')


cont = int(0)
lista = list()
lista_par = list()
lista_impar = list()
print(f'=' * 40 + f'\n{"LISTA PAR LISTA ÍMPAR":^40}\n' + f'=' * 40)
while True:
    lista.append(ler_int())
    while True:
        menu = str(input('Deseja Continuar? ')).strip().upper()
        if menu != '':
            menu = menu[0]
            if menu in 'SN':
                break
            else:
                print('entrada inválida, tente [S] ou [N]')
        else:
            print('vazio, tente [S] ou [N]')
    if menu in 'N':
        print(f'=' * 40 + f'\n{"FINALIZANDO":^40}\n' + f'=' * 40)
        break
    print(f'=' * 40)
for v in lista:
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
print(f'Lista origial: ', end='')
imp_lista(lista)
print(f'\nLista Par: ', end='')
imp_lista(lista_par)
print(f'\nLista Ímpar: ', end='')
imp_lista(lista_impar)
print(f'\nFIM\n=)')
