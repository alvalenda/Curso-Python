# EXERCÍCIO 96: Programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#               ( largura e comprimento ) e mostre a área do terreno.
from random import random


def area(largura, comprimento):
    return largura * comprimento


for i in range(10):
    print(f'Área do Terreno {i + 1:>2}:  {area(random()*100, random()*100):>8.2f} m²')
