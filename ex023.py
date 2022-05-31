# Excercício 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#                 ex.: Digite um número: 1834
#                      unidade: 4    dezena: 3  centena: 8  milhar: 1
num = int(10000)
while num > 9999:
    num = int(input('Entre com um número de 0 a 9999: '))
    num = abs(num)
let = str(num)
# let = let[0:5]
m = num // 1000
c = num // 100 % 10
d = num // 10 % 10
u = num % 10

print('Número: ', num)
print('unidade:\t', u)
print('dezena: \t', d)
print('centena:\t', c)
print('milhar: \t', m)
# print(let)
if len(let) == 1:
    print('\nunidade:\t', let[0])
    print('dezena: \t', 0)
    print('centena:\t', 0)
    print('milhar: \t', 0)
if len(let) == 2:
    print('\nunidade:\t', let[1])
    print('dezena: \t', let[0])
    print('centena:\t', 0)
    print('milhar: \t', 0)
if len(let) == 3:
    print('\nunidade:\t', let[2])
    print('dezena: \t', let[1])
    print('centena:\t', let[0])
    print('milhar: \t', 0)
if len(let) >= 4:
    print('\nunidade:\t', let[3])
    print('dezena: \t', let[2])
    print('centena:\t', let[1])
    print('milhar: \t', let[0])
