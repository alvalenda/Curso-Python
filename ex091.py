# EXERCÍCIO 91: Crie um programa onde 4 jogadores joguem um dado e tenham os resultados guardados em um dicionário.
#               No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
rolls = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
# print(rolls)
sorted_rolls = rolls.copy()
j1 = rolls['Jogador 1']
j2 = rolls['Jogador 2']
j3 = rolls['Jogador 3']
j4 = rolls['Jogador 4']
c1 = c2 = c3 = False
organiza = [j1, j2, j3, j4]
organiza.sort()
rolls.clear()

# Método 1
for i in range(len(organiza)-1, -1, -1):        # Looping começa no maior e vai até zero
    if organiza[i] == j1 and not c1:            # Se Elemento i da lista for j1 e 'Jogador 1' ainda não foi adicionado:
        rolls['Jogador 1'] = organiza[i]        # : Jogador 1 recebe elemento organiza[i]
        c1 = True                               # flag para marcar que Jogador 1 foi incluído no dicionário
    elif organiza[i] == j2 and not c2:
        rolls['Jogador 2'] = organiza[i]
        c2 = True
    elif organiza[i] == j3 and not c3:
        rolls['Jogador 3'] = organiza[i]
        c3 = True
    else:
        rolls['Jogador 4'] = organiza[i]
# print(rolls)
print(f'{" Método 1 ":#^25}')                 # Meu método de condicionais acima
for k, v in rolls.items():
    print(f'{k} rolou {v} no dado')         # Jogador X rolou VALOR

# Método 2 - Utilizando a função lambda
# sorted_rolls = {k: v for k, v in sorted(sorted_rolls.items(), key=lambda item: item[1])}  # organiza crescente
sorted_rolls = {k: v for k, v in sorted(sorted_rolls.items(), key=lambda item: item[1], reverse=True)}  # decrescente
print(f'\n{" Método 2 ":#^25}')                 # Utilizando função lambda com reverse
for k, v in sorted_rolls.items():
    print(f'{k} rolou {v} no dado')

# Método 3 utilizado pelo professor
# não gostei por isso deixarei todo comentado
# from operator import itemgetter
# ranking = list()
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print(ranking)
