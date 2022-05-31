# EXERCÍCIO 93: Programa que gerencia o aproveitamente de um jogador de futebol. Vai ler o nome do jogador e quantas
#               partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
#               será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
gols = list()
conta_partida = conta_gol = int(0)
print(f'='*60 + f'\n{"DESEMPENHO DOS ATLETAS - CRF":^60}' + f'\n' + f'='*60)
while True:
    nome = str(input(f'Nome do Jogador: ')).strip().title()
    if bool(nome):
        nome = nome[:30]
        break
    else:
        print(f'...')
jogador['Nome'] = nome
while True:
    while True:
        try:
            gol = int(input(f'Nº de Gols na partida {conta_partida + 1}: '))
        except ValueError:
            print(f'...')
        else:
            conta_partida += 1
            conta_gol += gol
            gols.append(abs(gol))
            break
    print(f'#' * 60)
    while True:
        menu = str(input(f'Adicionar mais jogos? ')).strip().upper()
        if bool(menu):
            menu = menu[0]
            if menu in 'SN':
                break
    if menu in 'N':
        print(f'*' * 60)
        break
    else:
        print(f'*' * 60 + '\n' + f'{f"JOGO ADICIONADO: PARTIDA {conta_partida+1}":^50}\n' + f'*' * 60)
jogador['Jogos'] = conta_partida
jogador['Gols'] = gols[:]
jogador['Aproveitamento'] = float(conta_gol / conta_partida)
for k, v in jogador.items():
    if k in 'Nome':
        print(f'{f"{k} do jogador":<19}: {v}')
    elif k in 'Jogos':
        print(f'{f"{k} disputados":<19}: {v}')
    elif k in 'Gols':
        print(f'{"Retrospecto de gols":<19}: ', end='')
        for g in v:
            print(f'{g}', end=', ')
        print()
    elif k in 'Aproveitamento':
        print(f'{"Gols por partida":<19}: {v:.2f}')
print(f'*' * 60 + f'\nFIM!!!')
