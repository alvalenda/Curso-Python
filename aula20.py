'''
    ==================================================== Aula 20 =======================================================
                                                    FUNÇÕES (PARTE i)
                        Funções são trechos de código que podem ser executados em momentos diferentes de nossos
                            códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo
                                             com parâmetros simples e múltiplos.
    ====================================================================================================================
'''
"""
pythoniseasy.com
pirple.com/python

def mostraLinha():
    print('-' * 30)

mostraLinha()
print('    BLA BLA BLA     ')
mostraLinha()

def titulo(msg):
    print(f'-' * 30)
    print(f'{"msg"}:^30')
    print(f'-' * 30)
titulo(SISTEMA DE ALUNOS)
>>>
>>>
>>>

-----------------------------------------
            SISTEMA DE ALUNOS
-----------------------------------------
<<<
============================== EMPACOTAR PARAMETROS ================================

def contador(*num):         # * é símbolo de desempacotar

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
EMPACOTA VALORES EM TUPLAS E PASSA A FUNÇÃO

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! TRABALHAR COM LISTAS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
dobra(valores)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

TODA PASSAGEM EM FUNÇÃO NO PYTHON É POR REFERÊNCIA
"""


def soma(a, b):
    print(f'{a + b}')


soma(7, 3)
soma(1, 2)
soma(0, 0)
soma(-1, -4)
soma(b=3, a=1)
soma(a=3, b=1)
print()


def contador(*num):
    print(len(num))
    for valor in num:
        print(f'{valor}', end=' ')
    print()


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def soma2(*val):
    s = 0
    for num in val:
        s += num
    print(f'Soma = {s}')


soma2(2, 3, 4, 56, 7)
soma2(3, 6)
soma2(1, 1, 3, -2)
# EXERCÍCIO 96: Programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#               ( largura e comprimento ) e mostre a área do terreno.
#
# EXERCÍCIO 97: Programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e
#               mostre uma mensagem com tamanho adaptável.
#
# EXERCÍCIO 98: Programa que tenha uma função chamda contador(), que receba três paraâmetros: ínicio, fim e passo e
#               realize uma contage. O programa deve realizar 3 contagens através da função criada: (crair o for)
#               a) De 1 até 10, de 1 em 1
#               b) De 10 até 0, de 2 em 2
#               c) Uma contagem personalizada
#
# EXERCÍCIO 99: Programa que tenha uma função chamada maior(), que receba várias parâmetros com valores inteiros.
#               O programa tem que analisar todos os valores e dizer qual deles é o maior.
#
# EXERCÍCIO 100: Programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somarPar(). A primeira
#                vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
#                todos os valores PARES sorteados pela função anterios.
#
