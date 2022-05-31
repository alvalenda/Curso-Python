# EXERCÍCIO 51: Programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
#               dessa progressão.
print('Entre com o primeiro termo e a razão de uma p.a.')
while True:
    try:
        p1 = int(input('Primeiro termo: '))
    except ValueError:
        print('Precisa ser um número inteiro')
    else:
        break
while True:
    try:
        r = int(input('Razão: '))
    except ValueError:
        print('Precisa ser um número inteiro')
    else:
        break
for i in range(p1, (p1 + r*10), r):
    print(i, end=' ⇀ ') if i < (p1 + r*9) else print(i)
