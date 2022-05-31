# EXERCÍCIO 95: Aprimore o exec. 093 para que ele funciona com vários jogadores, incluindo um sistema de visualização
#               de detalhes do aproveitamento de cada jogador.
jogador = dict()
gols = list()
lista = list()
conta_partida = conta_gol = int(0)
print(f'='*60 + f'\n{"DESEMPENHO DOS ATLETAS - CRF":^60}' + f'\n' + f'='*60)
while True:
    while True:
        nome = str(input(f'Nome do Jogador: ')).strip().title()
        if bool(nome):
            nome = nome[:30]
            break
        else:
            pass
    jogador['Nome'] = nome
    while True:
        try:
            cont = int(input(f'Nº de PARTIDAS: '))
        except ValueError:
            pass
        else:
            break
    for i in range(cont):
        while True:
            try:
                gol = int(input(f'Nº de Gols na partida {conta_partida + 1}: '))
            except ValueError:
                pass
            else:
                conta_partida += 1
                conta_gol += gol
                gols.append(abs(gol))
                print(f'{" PARTIDA ADICIONADA ":#^50}')
                break
    print(f'*' * 60 + '\n' + f'{f"JOGOS ADICIONADOS: {conta_partida} PARTIDAS":^50}\n' + f'*' * 60)
    jogador['Jogos'] = conta_partida
    jogador['Gols'] = gols[:]
    jogador['Aproveitamento'] = float(conta_gol / conta_partida)
    while True:
        menu = str(input(f'Adicionar mais JOGADORES? ')).strip().upper()
        if bool(menu):
            menu = menu[0]
            if menu in 'SN':
                break
    lista.append(jogador.copy())
    jogador.clear()
    gols.clear()
    conta_partida = conta_gol = int(0)
    if menu in 'N':
        print(f'*' * 60)
        break
    else:
        print(f'{" NOVO JOGADOR ":*^60}')
print(f'{"[ID]":<3}{" JOGADOR ":=^30}{" GOLS ":=^17}{"=":=^8}')
for j in range(len(lista)):
    print(f'[{j + 1}]\t\t{lista[j]["Nome"]:<30}\t{sum(lista[j]["Gols"]):^4}')
print(f'=' * 60)
# escolher qual jogador detalhar
print(f'DETALHAR QUAL JOGADOR?\t\t\t\t[0] PARA SAIR')
while True:
    while True:
        try:
            menu = int(input(f'[ID] do jogador: '))
        except ValueError:
            pass
        else:
            if abs(menu) <= len(lista):
                menu = abs(menu)
                break
    # se foi digitado 0 SAIR DO PROGRAMA
    if menu == 0:
        break
    # impressão detalhada
    print(f'*' * 60)
    print(f'{"Nome":<19}: {lista[menu -1]["Nome"]}')
    print(f'{"Jogos disputados":<19}: {lista[menu - 1]["Jogos"]}')
    print(f'{"Retrospecto de gols":<19}: ', end='')
    for g in lista[menu - 1]['Gols']:
        print(f'{g}', end=', ')
    print(f'\n{"Aproveitamento":<19}: {lista[menu - 1]["Aproveitamento"]:.2f} gols por partida')
    print(f'*' * 60)
print(f'*' * 60 + f'\nFIM!!!')
