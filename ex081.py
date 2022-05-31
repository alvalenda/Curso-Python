# EXERCÍCIO 81: Programa que lerá vários números e colocar em uma lista. Depois disso mostre:
#               (A) Quantos números foram digitados         (B) A lista de valores ordenada de gorma decrescente
#               (C) Se o valor 5 foi digitado e está ou não na lista.
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


cont = int(0)
lista = list()
print(f'=' * 40 + f'\n{"LISTA ORDENADA DECRESCENTE":^40}\n' + f'=' * 40)
while True:
    num = ler_int()
    if num not in lista:
        lista.append(num)
    while True:
        menu = str(input('Deseja Continuar? [S][N]')).strip().upper()
        if bool(menu):
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
print(f'Foram lidos um total de {cont} números e a lista contém {len(lista)} elementos.')
print(f'Lista em ordem decrescente: ', end='')
lista.sort(reverse=True)
for i in lista:
    print(f'{i}', end=' ')
print(f'\nO número 5 ESTÁ contido na lista') if 5 in lista else print(f'\nA lista NÃO contém o número 5.')
print(f'FIM!!!\n=)')
