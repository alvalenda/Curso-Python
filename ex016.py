# Exercício 16 - Um programa que leia um número REAL qqer e mostre na tela a sua porção inteira. ex.: 6.166 = 6

import math

num:  float
num = float(input('Entre com um número real:\t'))

print('A porção inteira de {} é {}' .format(num, math.trunc(num)))