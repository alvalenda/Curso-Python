'''
    ==================================================== Aula 19 =======================================================
                                                       DICIONÁRIOS
                        Dicionários são Variáveis Compostas que permitem armazenar vários
                         valores em uma mesma estrutura, acessíveis por chaves LITERAIS
    ====================================================================================================================
'''
"""
Tuplas      ()
Listas      []
Dicionários {}  >>> DECLARAÇÃO
dados = dict()
ou
dados = {}
estrutura iniciada
dados = { 'nome':'Pedro', 'idade':25 }
print(dados['nome'])    >>>     Pedro
print(dados['idade'])   >>>     25
dados['Gênero'] = 'M'
print(dados['Gênero'])  >>>     M
del dados['idade']                  # Remove o ELEMENTO 'IDADE', remove o valor junto. (claro)
dados.clear()                       # Apaga todo no dicionário, deixando-o vazio

filme = {   'título':'Star Wars',
            'ano':1977,
            'diretor':'George Lucas'
        }
        FILME
        ['Star Wars']  [ 1977 ] [ 'George Lucas' ]
            título       ano         diretor
print(filme.values())   >>>     'Star Wars' 1977 'George Lucas'
print(filme.keys())     >>>     'título'    'ano'   'diretor'
print(filme.items())    # imprime tudo, keys e values. chaves e valores.
for k, v in filme.items():
    print(f'O {k} é {v}')
>>> O titulo é Star Wars
>>> O ano é 1977
>>> O diretor é George Lucas
Posso criar uma lista para alocas dicionários (tuplas e listas tb) tudo com tudo.
locadora = [{'Star Wars', 1977 , 'George Lucas'}, {'Matrix', 1999, 'Wachoeski Sis'}, {'Avengers', 2012, 'focofi'}]
                            0                                      1                                2
dentro de 0, 1 e 2 da lista temos dicionários com suas respectivas chaves e valores
print(locadora[0]['ano'])       >>> 1977
print(locadora[1]['titulo'])    >>> Matrix
"""
pessoas = {'nome': 'Gustavo', 'genero': 'M', 'idade': 22}
print(pessoas.keys(), pessoas.values())
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.items())
for i in pessoas.values():
    print(f'{i}')
for k, v in pessoas.items():
    print(f'{k}: {v}')
del pessoas['genero']
for k, v in pessoas.items():
    print(f'{k}: {v}')
pessoas['nome'] = 'Flávio'
pessoas['peso'] = 99.99
for k, v in pessoas.items():
    print(f'{k}: {v}')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1.copy())   # Método interno de DICIONÁRIO QUE COPIA, ANÁLOGO AO [:] NAS LISTAS
brasil.append(estado2.copy())
print(brasil[0]['uf'], '-', brasil[1]['sigla'])     # kkkkkkk
for i in brasil:
    for k, v in i.items():
        print(f'{k}-{v}')
for i in brasil:
    for v in i.values():
        print(v, end=' ')
    print()
# EXERCÍCIO 90: Programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#               No final mostre o conteúdo da estrutura na tela.
#
# EXERCÍCIO 91: Crie um programa onde 4 jogadores joguem um dado e tenham os resultados guardados em um dicionário.
#               No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
#
# EXERCÍCIO 92: Programa leia NOME, ANO de NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com a idade) em um
#               dicionário, se por acaso o CTPS for diferente de ZERO, o dicionário receberá também
#               o ano de contratação e o salário. Calcule e acrescente, com quantos anos a passoa vai se aposentar.
#               35 anos de variação
#
# EXERCÍCIO 93: Programa que gerencia o aproveitamente de um jogador de futebol. Vai ler o nome do jogador e quantas
#               partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
#               será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
#
# EXERCÍCIO 94: Leia NOME, GENERO e IDADE de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
#               os dicionários em uma lista. No final, mostre:
#               (A) Quantas pessoas foram cadastradas       (B) A média de idade do grupo
#               (C) Uma lista com todas as mulheres         (D) Uma lista c/ todas as pessoas com idade acima da média
#
# EXERCÍCIO 95: Aprimore o exec. 093 para que ele funciona com vários jogadores, incluindo um sistema de visualização
#               de detalhes do aproveitamento de cada jogador.
#
