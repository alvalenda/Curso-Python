'''
    ==================================================== Aula 13 =======================================================
                                                ESTRUTURAS DE REPETIÇÃO - FOR -
                                    estruturas de 'laço' controladas pela função for
    ====================================================================================================================
'''
"""
for c in range(1,10):   >>> Para c no intervalo de 1 a 10
    passo
pega

for c in range(0,3):    >>> [*][]  [][]  [][] [][!]  
    passo
    pula
passo
pega

for c in range(0,3):    >>> [*][]  [%][]  [][] [%][!]
    if % is True:
        pega
    passo
    pula
passo
pega

"""
for c in range(0, 6):  # <<< vai de 0 a 5 == 6 vezes == range(6)
    print('Oi')

for c in range(0, 6, 2):  # de 0 a 5 PULANDO DE 2 EM 2
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f, p):
    print(c)
s = 0
for c in range(4):
    n = int(input('Digite um valor: '))
    s += n
print(s)

# EXERCÍCIO 46: Programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#               indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# EXERCÍCIO 47: Programa Programa que mestre na tela todos os números PARES no intervalo en 1 e 50
#

# EXERCÍCIO 48: Programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se
#               encontram no intervalo de 1 até 500.

# EXERCÍCIO 49: Refaça o ex009 mostrando a tabuada de um número que o usuário escolher, só agora
#               utilizando um laço FOR.

# EXERCÍCIO 50: Programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
#               Ignorando os ímpares

# EXERCÍCIO 51: Programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
#               dessa progressão.

# EXERCÍCIO 52: Programa que leia um número inteiro e diga se ele é ou não um número primo.
#

# EXERCÍCIO 53: Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando
#               os espaços.     ex.: 'APOS A SOPA' 'A SACADA DA CASA' 'A TORRE DA DERROTA' ''O LOBO AMA O BOLO'
#               'ANOTARAM A DATA DA MARATONA'

# EXERCÍCIO 54: Programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
#               atingiram a maioridade e quantas já são maiores.

# EXERCÍCIO 55: Programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
#

# EXERCÍCIO 56: Programa que leia o nome, idade e gênero de 4 pessoas. No final do programa mostre:
#               > A média de idade do grupo. > O nome do Homem mais velho > Quantos mulheres têm menos de 20 anos.

