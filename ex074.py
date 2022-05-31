# EXERCÍCIO 74: Programa que gere 5 números aleatórios e colocar numa tupla. Depois mostra a listagem de números gerados
#               e também indique o menor e o maior valor que estão contidos na tupla.
from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
lista = sorted(tupla)
print('Sortedos: ', end='')
for x in tupla:
    print(f'{x}', end=' ')
print('\nOrdenado: ', end='')
for x in lista:
    print(f'{x}', end=' ')
print(f'\nMaior: {max(tupla)} \nMenor: {min(tupla)}')  # max() dá o maior valor da TUPLA/LISTA e min() o menor
