# EXERCÍCIO 73: Cria uma tupla preenchida com os 20 primeiros colocados da Tabela do BRASILEIRÃO, na ordem de colocação
#               A) Apenas os 5 primeiros B) Os últimos 4 colocados C) Uma lista em ordem Alfabética D) EM que posição
#               fica a chapecoense (pegar trabela 2019)
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
          'Fortaleza', 'Goiás', 'Bahia', 'Vasquinho 2ª Divasco', 'Atlético-MG', 'Pague a Série B', 'Botafogo',
          'Ceará SC', 'Cruzeiro kkkkk', 'CSA', '\033[1;33mChapecoense\033[m', 'Avaí')
listaalfa = sorted(tabela)
print('=' * 50)
print(f'\t\t\tTABELA BRASILEIRÃO 2019:')
print('=' * 50)
for i, j in enumerate(tabela):
    print(f'{i + 1:2} - {j}')
print('=' * 50)
print(f'O G4: {tabela[0]}, {tabela[1]}, {tabela[2]} e {tabela[3]}.')
print(f'O Z4: {tabela[16]}, {tabela[17]}, {tabela[18]} e {tabela[19]}.')
print('=' * 50)
print(f'\t\t\tTABELA EM ORDEM ALFABÉTICA:')
print('=' * 50)
for i, j in enumerate(listaalfa):
    print(f'{i + 1:2} - {j}')
print('=' * 50)
pos = tabela.index('\033[1;33mChapecoense\033[m') + 1
print(f'A \033[1;33mChapecoense\033[m ficou na {pos}ª colocação no Campeonato Brasileiro 2019.')
