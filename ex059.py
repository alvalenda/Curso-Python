# EXERCÍCIO 59: Leia dois valores e mostre um menu na tela:
#               [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa
#               realizar a operação solicitada em cada caso.
def lernumero():
    palavra = ['Primeiro', 'Segundo']
    while True:
        try:
            a1 = float(input('Entre com o {} número: '.format(palavra[conta_c()])))
        except ValueError:
            print('O valor precisa ser um número. Tente novamente.')
        else:
            break
    return a1


def conta_c():
    global c
    if c % 2 == 0:
        c += 1
        return 0
    else:
        c += 1
        return 1


c = int(0)
n1 = lernumero()
n2 = lernumero()
menu = 0
while menu != 5:
    print('[1]Somar\t[2]Multiplicar\n[3]Maior\t[4]Novos Números\t[5]Sair')
    while True:
        try:
            menu = int(input('Ação: '))
        except ValueError:
            print('Entre com uma Opção Existente no menu.')
        if 0 < menu < 6:
            break
        else:
            print('Entre com uma Opção Existente no menu.')
    if menu == 1:
        print('{:.2f} + {:.2f} = {:.2f}'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('{:.2f} x {:.2f} = {:.2f}'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 >= n2:
            print('{} é o maior número'.format(n1))
        else:
            print('{} é o maior número'.format(n2))
    elif menu == 4:
        n1 = lernumero()
        n2 = lernumero()
print('Um total de {} números foram lidos no processo'.format(c))   # podia trocar td pra fstrigns depois
print('FIM!!!!!!!!!!!')
