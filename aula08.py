'''
    ==================================================== Aula 08 =======================================================
                                                  UTILIZAÇÃO DE MÓDULOS
                                              IMPORTAÇÃO DE MÓDULOS E MÉTODOS
    ====================================================================================================================
'''
"""
Para importar Módulos se utiliza o comando 'import'
ex.: import math    >>>     importa o módulo com métodos matemáticos
(É o equivalente ao adicionar bibliotecas em C)

Ao importar um módulo você traz com ele todas as uas funções (métodos) e os acessa atraves do comando: "módulo.método"
ex.: math.sqrt()   >>>  para chamar o método sqrt do módulo math

É possível importar apenas métodos específicos de dentro das bibliotecas através do comando from xxxx import
ex.: from math import sqrt, floor, ceil, pow
Desta maneira só é importado o método que for especificado e não é necessária a chamada do módulo ao chamar a função
ex.: pow(a, b), floor(a), ceil(a), sqrt(a)       >>>        note que o math. não é chamado quando se importa pelo from
"""

# Exercícios Utilizando Bibliotecas (math provavelmente + random + ). Módulos

# Exercício 16 - Um programa que leia um número REAL qqer e mostre na tela a sua porção inteira. ex.: 6.166 = 6

# Exercício 17 - Um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcule
#                e mostre o comprimento da hipotenusa.   (utilizarei em cm)

# Exercício 18 - Um programa que leia um ângulo qqer e mostre na tela o valor do seno, cosseno e tangente.

# Exercício 19 - Um professor quer sortear um dos seus quatro alunos pra apagar o quadro. Faça um programa que ajude
#                o professor, lendo o nome dos alunos e escrevendo o nome do escolhido

# Exercício 20 - O mesmo professor o ex.19 quer sortear a ordem de apresentação de um trabalho dos alunos. Faça um
#                programa que leia o nome dos quatro alunos e mostre a lista com a ordem sorteada.

# Exercício 21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#                descorbrir o módulo que faz isso, vou ter que pesquisar. bjos
