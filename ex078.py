# EXERCÍCIO 78: Programa que leia 5 valores númericos e guarde-os em uma LISTA. No final, mostre qual foi o maior e
#               o menor valor digitado e as suas respectivas posições na lista.
def ler_int():
    global cont
    while True:
        try:
            n = int(input(f'Entre com {cont}º o número: '))
        except ValueError:
            print('valor inválido, tenta novamente...')
        else:
            cont += 1
            return n


lista = list()
cont = int(1)
for i in range(5):
    lista.append(ler_int())
for i in lista:
    print(f'{i}', end=' ')
print(f'\nMenor valor da lista é: {min(lista)}\nEle foi digitado na leitura:', end=' ')
for x, y in enumerate(lista):
    if y == min(lista):
        print(f'{x + 1}', end=' ')
print(f'\nMaior valor da lista é: {max(lista)}\nEle foi digitado na leitura:', end=' ')
for x, y in enumerate(lista):
    if y == max(lista):
        print(f'{x + 1}', end=' ')
print(f'')
