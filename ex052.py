# EXERCÍCIO 52: Programa que leia um número inteiro e diga se ele é ou não um número primo.
#
from math import sqrt, floor
while True:
    try:
        num = int(input('Número: '))
    except ValueError:
        print('Numero inteiro seu arrombado!')
    else:
        break
if num > 1:
    print(floor(sqrt(num)))
    # a composite number must have a factor less than the square root of that number. Otherwise, the number is prime.
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            print('{} não é um número primo.'.format(num))
            print('{} x {:.0f} = {}'.format(i, num / i, num))
            break
    else:
        print('{} é um número primo.'.format(num))
else:
    print('{} não é primo.'.format(num))
