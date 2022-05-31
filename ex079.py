# EXERCÍCIO 79: Programa que se possa entrar com VÁRIOS NÚMEROS (while) e os cadestre numa lista. Caso o número já
#               exista na lista, ele não será adicionado. No final serão exibidos todos os valores únicos digitados
#               em ordem crescente.
def ler_int():
    global cont
    while True:
        try:
            n = int(input(f'Entre com {cont + 1}º o número: '))
        except ValueError:
            print('valor inválido, tenta novamente...')
        else:
            cont += 1
            return n


lista = list()
cont = int(0)
print(f'=' * 40 + f'\n{"LISTA ORDENADA SEM REPETIÇÃO":^40}\n' + f'=' * 40)
while True:
    num = ler_int()
    if num not in lista:
        # print(f'pop!')
        lista.append(num)
    while True:
        menu = str(input('Deseja continuar? [S][N] ')).strip().upper()
        if menu != '':
            menu = menu[0]
            if menu in 'SN':
                break
            else:
                print('entrada inválida, tente novamente...')
        else:
            print('vazio, tente novamente...')
    if menu in 'N':
        print(f'=' * 40)
        break
    print(f'=' * 40)
lista.sort()
print(f'Lista ordenada sem repetição: ', end='')
for i in lista:
    print(f'{i}', end=' ')
print(f'\nA lista contém {len(lista)} números de um total de {cont} entradas.')
