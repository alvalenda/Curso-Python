# EXERCÍCIO 108: Aula 22
import uteis.dado as dado
import uteis.moeda as mo
from random import random

num = dado.leia_float('Valor em Reais: ')
aum = random()*100
red = random()*100
print(f'Aumento  de {aum:^5.1f}%: {mo.moeda(mo.aumentar(num, aum))}')
print(f'Redução  de {red:^5.1f}%: {mo.moeda(mo.diminuir(num, red))}')
print(f'Dobro    de {num:^6}: {mo.moeda(mo.dobrar(num))}')
print(f'Metade   de {num:^6}: {mo.moeda(mo.metade(num))}')
