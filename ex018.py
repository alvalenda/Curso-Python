# Exercício 18 - Um programa que leia um ângulo qqer e mostre na tela o valor do seno, cosseno e tangente.
# import math
from math import radians, sin, cos, tan
teta:  float
sen:   float
cos:   float
tan:   float
teta = float(input('Entre com um ângulo:\t'))

"""
sen = math.sin(math.radians(teta))
cos = math.cos(math.radians(teta))
tan = math.tan(math.radians(teta))
"""
sen = sin(radians(teta))
cos = cos(radians(teta))
tan = tan(radians(teta))

# print('Valores para o ângulo de {:.2f}° = {:.2f}rad' .format(teta, math.radians(teta)))
print('Valores para o ângulo de {:.2f}° = {:.2f}rad' .format(teta, radians(teta)))
print('Seno:\t\t{:.4f} \nCosseno:\t{:.4f} \nTangente:\t{:.4f}' .format(sen, cos, tan))

