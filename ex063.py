# EXERCÍCIO 63: Leia um número 'n' inteiro qqer e mostre na tela os 'n' primeiros elementos de uma sequência de
#               Fibonacci.
#               ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 ...
print('\033[7m'+'*'*20+'< FIBONACCI >'+'*'*20+'\033[m')
x = 0
y = z = 1
n = 0
while True:
    try:
        elementos = abs(int(input('Mostrar quantos elemetos da sequência? ')))
    except ValueError:
        print('Número né meu amigo...')
    else:
        break
while n < elementos:
    print(x, end=' ')
    n += 1
    x = y
    y = z
    z = x + y
