# EXERCÍCIO 87: Aprimore o [86] mostrando ao final:
#               [A] A SOMA de todos os valores pares digitados [B] A Soma dos valores da terceira COLUNA
#               [C] O maior valor da segunda LINHA
matriz = list()
linha = list()
soma_par = soma_3Col = ic = int(0)
print(f'\033[7m' + f'=*' * 25 + f'\033[m' + f'\n\033[7m{"MATRIZ 3X3":^50}\033[m\n' + f'\033[7m=*' * 25 + f'\033[m')
for i in range(3):
    for j in range(3):
        while True:
            try:
                valor = int(input(f'Elemento ({i + 1},{j + 1}): '))
            except ValueError:
                print(f'inválido...')
            else:
                break
        linha.append(valor)       # linha recebe 3 valores
    matriz.append(linha[:])       # ao terminar o for J matriz recebe cópia da linha
    linha.clear()                 # limpa a lista linha e volta pra mais um loop em j
print(f'{"="}' * 45)
for j in matriz:
    for i in j:
        print(f'{i:^3}', end=' ')
        if i % 2 == 0:              # se par >> acumula
            soma_par += i
        if ic == 2:                 # se IC == 2 está na terceira coluna da matriz >> acumula
            soma_3Col += i
        ic += 1                     # contador da posição da coluna. 'I_Counter' kkk
    ic = 0                          # volta a coluna pra posição 0
    print()
print(f'{"="}' * 45)
print(f'Soma de todos os valores pares:\t{soma_par}')
print(f'Soma dos valores da 3ª Coluna:\t{soma_3Col}')
print(f'O Maior valor da Segunda Linha:\t{max(matriz[1])}')
