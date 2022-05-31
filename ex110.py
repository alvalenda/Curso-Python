# EXERCÍCIO 110: Aula 22
from uteis import dado
from uteis import moeda as mo

num = dado.leia_float('Valor em R$: ')
aum = dado.leia_float('Aumento em %: ')
red = dado.leia_float('Redução em % ')
mo.resumo(num, aum, red)
