# Exercício 20 - O mesmo professor o ex.19 quer sortear a ordem de apresentação de um trabalho dos alunos. Faça um
#                programa que leia o nome dos quatro alunos e mostre a lista com a ordem sorteada.
"""
    from collections import namedtuple
    Something = namedtuple('Something', 'a b c')
    a = Something(1, 2, 4)
    a.c
    4
"""
from random import sample, shuffle
from collections import namedtuple

lista = namedtuple('lista', 'a b c d')
s = ', ' # separador para função join imprimir os elementos da string de forma limpa
a1: str
a2: str
a3: str
a4: str
a1 = str(input('Nome do Primeiro aluno:\t'))
a2 = str(input('Nome do Segundo aluno:\t'))
a3 = str(input('Nome do Terceiro aluno:\t'))
a4 = str(input('Nome do Quarto aluno: \t'))

alunos = lista(a1, a2, a3, a4)
alunas = [a1, a2, a3, a4]

print('Lista dos alunos: {}' .format(s.join(alunos)))
print('Lista ordenada aleatoriamente: {}' .format(s.join(sample(alunos, 4))))

# Outra forma de fazer é embaralhando a lista de alunos com o método shuffle
shuffle(alunas)
print('Lista aleatória (shuffle): {}' .format(s.join(alunas)))
# conclusão: namedtuple é muito bom mas para esse exercício não se faz necessário, foi um ótimo aprendizado
# O separador na hora de imprimir deixa a saída mais bela, mas tb não é necessário. A impressão simples da lisa Alunas
# serveria. Enfim, ótimo exercício.
