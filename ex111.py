# EXERCÍCIO 111: Aula 22
from uteis import dado
from uteis import moeda as mo
from random import random

num = dado.leia_moeda('Valor em R$: ')      # testando função criada para ex112
aum = random()*100
red = random()*100
mo.resumo(num, aum, red)

