# EXERCÍCIO 80: Programa em que o usuário entre com 5 valores números e cadastre-os em uma lista, JÁ NA POSIÇÃO CORRETA
#               DE INSERÇÃO (sem utilizar o sort()). Ao final mostre a lista ordenada na tela.
def ler_int():
    global cont
    while True:
        try:
            n = int(input(f'Entre com {cont + 1}º número: '))
        except ValueError:
            print('valor inválido, tenta novamente...')
        else:
            cont += 1
            return n


cont = int(0)
lista = list()
for i in range(5):
    valor = ler_int()
    if len(lista) == 0:                         # Podia ter testado se i == 0 tb, ou um not bool(lista)... foda-se
        lista.append(valor)
    else:
        indice = 0                              # contador da posição do índice ao varrer a lista
        for j in lista:
            if valor <= j:                      # Para quando o número lido for menor que o valor atual de J
                # print('1', indice)
                lista.insert(indice, valor)     # Adiciona o valor lido no índice atual de J na Lista.
                break                           # Quebra o FOR (senão entra em looping infinito kkk)
            elif (indice + 1) == len(lista):    # Se chegar ao final da LISTA e NUM ainda for O MAIOR elemento...
                # print('2', indice)
                lista.append(valor)             # ... adicionar NUM no final da LISTA
                break                           # Quebrar o looping inf
            indice += 1                         # incrementa o marcador do índice
print(f'Lista ordenada na entrada: ', end='')
for i in lista:
    print(f'{i}', end=' ')
print(f'\nBoa noite!')
