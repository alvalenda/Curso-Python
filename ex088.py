# EXERCÍCIO 88: Programa que ajude um jogador da MEGA SENA a criar palpites. O programa pergunta quantos jogos serão
#               gerados e vai sortear 6 números entre 1 e 60 para cada jogo (sem repetição). Cadastrando tudo em uma
#               lista composta.
from random import randint
palpites_mega = list()
jogo = list()
cont_el = cont_jogo = int(0)
print(f'\033[7m=*' * 25 + f'\033[m' + f'\n\033[7m{"GERADOR DA MEGASENA":^50}\033[m\n' + f'\033[7m=*' * 25 + f'\033[m')
while True:
    try:
        n_jogos = int(input(f'Gerar quantos jogos? '))
    except ValueError:
        print(f'inválido...')
    else:
        if n_jogos > 0:
            break
        else:
            print(f'mínimo de 1 palpite...')
for j in range(n_jogos):
    for i in range(6):
        while True:
            n = randint(1, 60)
            if n not in jogo:
                jogo.append(n)
                break
    jogo.sort()
    palpites_mega.append(jogo[:])
    jogo.clear()
for j in palpites_mega:
    cont_jogo += 1
    print(f'{cont_jogo:>3}º palpite:', end=' ')
    for i in j:
        print(f'{i:>2}', end=', ') if cont_el < 5 else print(f'{i:^2}')
        cont_el += 1
    cont_el = 0
print(f'BOA SORTE!!!\t\t=)')
