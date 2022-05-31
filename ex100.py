# EXERCÍCIO 100: Programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somarPar(). A primeira
#                vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
#                todos os valores PARES sorteados pela função anterios.
from random import randint


def sorteio(lst):
    lst.clear()
    for a in range(5):
        a = randint(0, 9)
        lst.append(a)


def soma_par(lst):
    soma = int(0)
    for p in lst:
        if p % 2 == 0:
            soma += p
    return soma


numeros = list()
sorteio(numeros)
print(f'NÚMEROS SORTEADOS: ', end='')
for i in numeros:
    print(f'{i}', end=' ')
print()
print(f'A SOMA DOS NÚMEROS PARES SORTEADOS VALE: {soma_par(numeros)}')
