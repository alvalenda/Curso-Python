# EXERCÍCIO 98: Programa que tenha uma função chamda contador(), que receba três paraâmetros: ínicio, fim e passo e
#               realize uma contage. O programa deve realizar 3 contagens através da função criada: (crair o for)
#               a) De 1 até 10, de 1 em 1
#               b) De 10 até 0, de 2 em 2
#               c) Uma contagem personalizada
from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo *= -1
        while inicio >= fim:
            print(f'{inicio}', end=' ')
            inicio += passo
            sleep(0.3)
    else:
        while inicio <= fim:
            print(f'{inicio}', end=' ')
            inicio += passo
            sleep(0.3)
    print()


contador(1, 10, 1)          # (A)
contador(10, 0, 2)          # (B)
for x in range(3):
    while True:
        try:
            if x == 0:
                i = int(input(f'INÍCIO: '))
            elif x == 1:
                f = int(input(f'FIM: '))
            else:
                p = int(input(f'PASSO: '))
        except ValueError:
            pass
        else:
            break
contador(i, f, p)          # (C)
