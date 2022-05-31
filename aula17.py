'''
    ==================================================== Aula 17 =======================================================
                                                    LISTAS (parte 1)
                       Listas são Variáveis Compostas e imutáveis que permitem armazenar vários
                          valores em uma mesma estrutura, acessíveis por chaves individuais
    ====================================================================================================================
'''
"""
LISTAS [] <- COLCHETES
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Picolé'
print(lanche) >>> ['Hamburguer', 'Suco', 'Pizza', 'Picolé']
Pois listas são MUTÁVEIS
lanche.append('Biscoito')  # Insere um valor no final da Lista, coloca como uma pilha.
print(lanche) >>> ['Hamburguer', 'Suco', 'Pizza', 'Picolé', 'Biscoito']
lanche.insert(0, Hotdog)  # Insere um valor na lista em qualquer posição, 0 nesse caso empurrando as outras chaves.
print(lanche) >>> ['Hotdog', 'Hamburguer', 'Suco', 'Pizza', 'Picolé', 'Biscoito']
del lanche[3]  # usado para remover o valor N da lista, nesse caso o que está no índice 3
lanche.pop(3)  # geralmente usado pra remover o valor do último índice (topo da pilha) mas pode passar parâmetro tb
lanche.remove('Pizza')  # Com Remove vc REMOVE PELO VALOR (conteúdo) e não pela chave (índice).
com qualquer dos 3 métodos acima o resultado da aplicação seria esse:
print(lanche) >>> ['Hamburguer', 'Suco', 'Picolé', 'Biscoito']
lanche.pop() # É muito bom para remover o último elemento, no caso da lista Lanche removeria o Biscoito
print(lanche) >>> ['Hamburguer', 'Suco', 'Picolé']
lanche.remove('Pizza') # Note que não há o valor pizza, se isso for executado resulta num erro da linguagem que pode
                       # Ser tratado, verificando antes."if 'Pizza' in lance: lanhce.remove('Pizza')" COISA LINDA
# Utilizando a função list() + range para criar uma lista:
valores = list(range(4,11))
print(valores) >>> [4, 5, 6, 7, 8, 9, 10]
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores) >>> [8, 2, 5, 4, 9, 3, 0]
valores.sort()  # Mesmo .sort() das tuplas é válido, porém altera a lista
print(valores) >>> [0, 2, 3, 4, 5, 8, 9]
valores.sort(reverse=True)
print(valores) >>> [9, 8, 5, 4, 3 ,2 ,0]
len(valores)    # retorna 7 neste caso, mesma utilidade de string, tuplas e etc... =)
"""
num = [2, 5, 9, 1]
num[2] = 3                  # altera o valor do índice 2 para 3. O 9 passa a ser 3
num.append(7)               # insere 7 no como último valor da lista
print(num)
num.sort()                  # ordena de forma crescente
print(num)
num.sort(reverse=True)      # ordem decrescente
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)            # insere o valor 0 na posição do (índice/chave) 2
print(num)
num.pop()                   # remove o último elemento
print(f'pop(): {num}')
num.pop(2)                  # remove o elemento no índice 2
print(f'pop(2): {num}')
num.remove(2)               # remove a primeira ocorrência do índice com VALOR 2 (se existe e tem mais de 1)
for v in num:               # Imprimindo VALORES
    print(f'{v}', end=' ')
print('')
for c, v in enumerate(num):     # Imprimindo CHAVES e VALORES
    print(f'Na posição {c} encontrei o valor {v}')
valores = list()
for cont in range(5):
    valores.append(int(input('Digite um valor: ')))  # leitura de 5 valores num lista
for c, v in enumerate(valores):                      # Imprimindo CHAVES e VALORES
    print(f'Na posição {c} encontrei o valor {v}')
a = [2, 3, 4, 5]
b = a
b[2] = 8            # AQUI ALTERA O VALOR NAS DUAS LISTAS POIS QUANDO IGUALA SE FAZ UMA LIGAÇÃO ENTRE AS LISTAS
#                   # PARA COPIAR UTILIZE ESSE MÉTODO:
a = [2, 3, 4, 5]
c = a[:]            # AQUI C recebe TODOS OS ELEMENTOS de A, mas NÃO é IGUAL a A!!!! =)
b = a
b[2] = 8
print(f'a:{a}')
print(f'b:{b}')     # NOTEM A DIFERENÇA !!! =)
print(f'c:{c}')

# EXERCÍCIO 78: Programa que leia 5 valores númericos e guarde-os em uma LISTA. No final, mostre qual foi o maior e
#               o menor valor digitado e as suas respectivas posições na lista.
#
# EXERCÍCIO 79: Programa que se possa entrar com VÁRIOS NÚMEROS (while) e os cadestre numa lista. Caso o número já
#               exista na lista, ele não será adicionado. No final serão exibidos todos os valores únicos digitados
#               em ordem crescente.
#
# EXERCÍCIO 80: Programa em que o usuário entre com 5 valores números e cadastre-os em uma lista, JÁ NA POSIÇÃO CORRETA
#               DE INSERÇÃO (sem utilizar o sort()). Ao final mostre a lista ordenada na tela.
#
# EXERCÍCIO 81: Programa que lerá vários números e colocar em uma lista. Depois disso mostre:
#               (A) Quantos números foram digitados         (B) A lista de valores ordenada de forma decrescente
#               (C) Se o valor 5 foi digitado e está ou não na lista.
#
# EXERCÍCIO 82: Programa que vai ler vários números e colocar em uma lista. Depois, crie duas listas extras que vão
#               conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#               ao final, mostre o conteúdo das três listas geradas.
#
# EXERCÍCIO 83: Programa em que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
#               analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#               (creio que seja só contar os parênteses abertos e fechados e a ordem '(' antes de ')' )
#
