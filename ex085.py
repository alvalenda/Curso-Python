# EXERCÍCIO 85: Usuário pode digitar SETE valores numéricos e cadastre-os em uma única lista que mantenha separados os
#               valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
num = list()
par = list()
impar = list()
palavra = ('Pares', 'Ímpares')
num.append(par)
num.append(impar)
cont = int(0)
for i in range(7):
    while True:
        try:
            n = int(input(f'{cont + 1}ª Número: '))
        except ValueError:
            print(f'inválido...')
        else:
            cont += 1
            break
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
num[0].sort()
num[1].sort()
cont = int(0)
for x in num:                       # Imprimir as duas Listas PAR depois IMPAR
    for y in x:
        if cont == 0 or cont == 1:
            print(f'Lista de números {palavra[cont]:^7}:', end=' ')
            cont = 2
        print(f'{y}', end=' ')
    print()
    cont = 1
print(f'\nFIM!')
