# EXERCÍCIO 102: Programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indicará o número
#                a calcular e o outro chamado show, que será o valor lógico (opcional) indicando se será mostrado ou
#                não na tela o precesso de cálculo do fatorial.
from random import randint
from time import sleep


def fatorial(n=1, show=False, pri=True):
    if n == 1 or n == 0:
        sleep(0.2) if show else ()
        print(f' x {1} =', end=' ') if show else ()
        return 1
    if show and pri:
        sleep(0.2)
        print(f'{n}', end='') if show else ()
    else:
        sleep(0.2) if show else ()
        print(f' x {n}', end='') if show else ()
    return n * fatorial(n - 1, show, False)


mostra = [False, True]
num = int(0)
for _ in range(25):
    sleep(0.5)
    num = randint(0, 30)
    logic = mostra[randint(0, 1)]
    print(f'{f"[{logic}]":>7} {num:>2}! = ', end='')
    print(f'{fatorial(num, mostra[logic]):,}')
