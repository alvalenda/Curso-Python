'''
    ==================================================== Aula 16 =======================================================
                                                          TUPLAS
                            tuplas são Variáveis Compostas e imutáveis que permitem armazenar vários
                              valores em uma mesma estrutura, acessíveis por chaves individuais
    ====================================================================================================================
'''
"""
    a = [] = variável simples
    a = [0][1][2][3] = variável compostas - 0, 1, 2, 3, 4 são índices 
    Tuplas são uma forma de variável compostas (armazenam vários valores)
    Existem 03 tipos de variáveis compostas no Python
        * Tuplas
        * Listas
        * Dicionários
    lanche = [hamburguer][suco][pizza][pudim]
    print(lanche[2])    -> pizza
    print(lanche[0:2])  -> hamburguer suco
    print(lanche[1:])   -> suco pizza pudim
    print(lanche[-1])   -> pudim (espelhado e invertido) pudim é 3 e 1, hamburguer é 0 e -4
    len(lanche)         -> Nª elementos de lanche -> 4
    for c in lanche:    -> cria uma variável *simples* que atribui um valoir de lanche a cada ciclo
        print(c)
    ---------------------------------------------> AS TUPLAS SÃO IMUTÁVEIS <-----------------------------------------
  
"""
# () = TUPLA, [] = LISTA, {} = DICIONÁRIO
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  # a partir de python 3.5 não precisa de (),
# mas usaremos para melhor compreensão
print(lanche)
print(lanche[2:])
print(lanche[:2])
print(lanche[::-1])
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(f'Doidera, comi pra caralho!')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))   # mostra a tupla de forma ordenada (não altera)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b   # a + b != b + a pq concatena
print(c, c.count(5), len(c), c.index(8))  # index mostra a posição daquele valor.
pessoa = ('Gustavo', 39, 'M', 99.88)  # aceita variáveis distintas dentro da tupla (vetor)
print(pessoa)
del pessoa  # tupla é imutável mas PODE SER DELETADA. ISSO serve pra qqer variável. ou del(pessoa)

# EXERCÍCIO 72: Programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#               O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
#
# EXERCÍCIO 73: Cria uma tupla preenchida com os 20 primeiros colocados da Tabela do BRASILEIRÃO, na ordem de colocação
#               A) Apenas os 5 primeiros B) Os últimos 4 colocados C) Uma lista em ordem Alfabética D) EM que posição
#               fica a chapecoense (pegar trabela 2019)
#
# EXERCÍCIO 74: Programa que gere 5 números aleatórios e colocar numa tupla. Depois mostra a listagem de números gerados
#               e também indique o menor e o maior valor que estão na tupla.
#
# EXERCÍCIO 75: Programa que leia 4 valores pelo teclado e guardar numa tupla. Mostre: (A) Quantas vezes apareceu o
#               valor 9 (B) Em que posição foi digitado o primeiro 3 (C) quais foram os números pares.
#
# EXERCÍCIO 76: Programa que tenha uma tupla única com nomes de produtes e seus respectivos preços na sequênia.
#               Mostre uma listagem de preços, organizando os dados em forma tabular
#
# EXERCÍCIO 77: Programa que tenha uma tupla com várias palavras. Depois Mostrar para cada palavras quais são as suas
#               vogais.
