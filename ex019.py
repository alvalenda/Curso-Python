# Exercício 19 - Um professor quer sortear um dos seus quatro alunos pra apagar o quadro. Faça um programa que ajude
#                o professor, lendo o nome dos alunos e escrevendo o nome do escolhido

"""
>>> from collections import namedtuple
>>> Something = namedtuple('Something', 'a b c')
>>> a = Something(1, 2, 4)
>>> a.c
4
"""
import random
# random.choice()
# random.choices()
# random.random()
# random.sample(pop, 1)
alunos: str
a:  str
b:  str
c:  str
d:  str

a = str(input('Nome do primeiro aluno:\t'))
b = str(input('Nome do segundo aluno:\t'))
c = str(input('Nome do terceiro aluno:\t'))
d = str(input('Nome do quarto aluno:\t'))

alunos = [a, b, c, d]
separador = ', '        # define o q vai seprar cada termo ao imprimir com join
# alunos = list(map(str, input("Enter a multiple value: ").split(None, 4)))

print("Lista dos quatro estudantes: ", separador.join(alunos))
# print('0\t=\t', x[0])
# print('1\t=\t', x[1])
# print('2\t=\t', x[2])
# print('3\t=\t', x[3])
print('Aluno sorteado para apagar o quadro: {}' .format(separador.join(random.sample(alunos, 1))))
print('Aluno sorteado pelo método 2: {}' .format((random.choice(alunos))))
