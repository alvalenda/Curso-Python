# Exercício 17 - Um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcule
#                e mostre o comprimento da hipotenusa.   (utilizarei em cm)
from math import hypot
# import math
co: float
ca: float
hp: float

print('Hipotenuzômetro Plus Plus!!!\nEntre com os valores dos Catetos Oposto e Adjacente de um Triângulo Retângulo.')
co = float(input('Cateto Oposto (cm):\t'))
ca = float(input('Cateto Adjacente (cm):\t'))

hp = hypot(co, ca)
# hp = math.hypot(co, ca)
# >>> hp = (co * co + ca * ca)**0.5


print('A hipotenuse des triângulo retângulo vale: {:.4f}cm' .format(hp))
print('A hipotenusa calculada na mão vale: {:.4f}cm' .format((co * co + ca * ca)**0.5))