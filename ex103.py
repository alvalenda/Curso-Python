# EXERCÍCIO 103: Uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos
#                gols ele marcou. Deverá ser capaz de mostrar a ficha do jogador, mesmo que não tenha sido informado
#                corretamente.
from random import randint
from time import sleep


def ficha(nome='DESCONHECIDO', gols=0):
    print(f'{nome: <18} efetuou {gols:^3} gols.')


nomes = ['Gabriel Barbosa',
         'Júlio César',
         'Bruno Henrique',
         'Rafinha Arrombaran',
         'Maurício Isla',
         'De Arrascaeta'
         ]
gol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]
for _ in range(30):
    sleep(0.6)
    n1 = randint(0, 5)
    n2 = randint(0, 5)
    if n1 > 0 and n2 > 0:
        ficha(nomes[randint(0, len(nomes) - 1)], gol[randint(0, len(gol) - 1)])
    elif n1 > 0:
        ficha(nomes[randint(0, len(nomes) - 1)])
    elif n2 > 0:
        ficha(gols=gol[randint(0, len(gol) - 1)])
    else:
        ficha()
print(f'FIM!!!')
