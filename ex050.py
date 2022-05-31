# EXERCÍCIO 50: Programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
#               Ignorando os ímpares
pares = []
acumula = 0
for i in range(6):
    while True:
        try:
            n = int(input('Entre com um número Inteiro: '))
        except ValueError:
            print('Precisa ser um valor inteiro')
        else:
            break
    if n % 2 == 0:
        pares.insert(len(pares), n)  # insere 'n' na posição do primeiro argumento (no final da lista)
        acumula += n                 # acumula somente os valores pares
print('Números pares:', end=' ')
for x in pares:
    print('{}'.format(x), end=' ')
print('\nSoma dos pares: {}'.format(acumula))
