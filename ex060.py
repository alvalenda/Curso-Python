# EXERCÍCIO 60: Leia um número qualquer e mostre o seu fatorial.
#                  ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
# A biblioteca MATH tem função fatorial. Chama FACTORIAL. from math import factorial   n = factorial(n) gg
from math import factorial


def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)


while True:
    num = int(-1)
    try:
        num = int(input('Deseja o fatorial de qual número? '))
    except ValueError:
        print('Precisa ser um número INTEIRO não NEGATIVO. Tente novamente...')
    if num >= 0:
        break
    else:
        print('Precisa ser um número INTEIRO não NEGATIVO. Tente novamente...')
# método 1 = função recursiva
print('{}! = {}'.format(num, fatorial(num)))
# método 2 = laço lógico de repetição WHILE
fat = 1
num2 = num
while num > 1:
    fat *= num
    num -= 1
print('{}! = {}'.format(num2, fat))

# método 3 = importando o método da biblioteca math kkk
print('{}! = {}'.format(num2, factorial(num2)))
