# EXERCÍCIO 109: Aula 22
from uteis import dado
import uteis.moeda as mo
from random import random

num = dado.leia_float('Valor em R$: ')
aum = random()*100
red = random()*100
print(f'Aumento  de {aum:^5.1f}%: {mo.aumentar(num, aum, True)}')
print(f'Redução  de {red:^5.1f}%: {mo.diminuir(num, red, True)}')
print(f'Dobro    de {num:^6}: {mo.dobrar(num, True)}')
print(f'Metade   de {num:^6}: {mo.metade(num, True)}')
