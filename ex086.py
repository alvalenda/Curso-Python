# EXERCÍCIO 86: Crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final, imprima a matriz na tela com a
#               formatação correta.
matriz = list()
linha = list()
print(f'=*' * 25 + f'\n{"MATRIZ 3X3":^50}\n' + f'=*' * 25)
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
for i in matriz:
    for j in i:
        print(f'{j:^3}', end=' ')
    print()
