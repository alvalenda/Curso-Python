'''
    ==================================================== Aula 18 =======================================================
                                                    LISTAS (parte 2)
                       Listas são Variáveis Compostas e mutáveis que permitem armazenar vários
                          valores em uma mesma estrutura, acessíveis por chaves individuais
    ====================================================================================================================
'''
"""
dados = list()
dados.append('Pedro')
dados.append('25')
['Pedro', 25]

pessoas = list()
pessoas.append(dados[:])    # Pega uma cópia de dados e faz append em pessoas!
           0      1       0      1       0     1
pessoas[['Pedro', 25], ['Maria', 19], ['João', 32]]
              0              1              2
Como declarar essa estrutura toda de uma vez só: pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
listas compostas, listas dentro de listas. 
print(pessoas[0][0])    # pessoas zero = estrutura com [0] Pedro e [1] 25
>>> Pedro
print(pessoas[1][1])  
>>> 19
print(pessoas[2][0])
>>>João
print(pessoas[1])
>>> ['Maria', 19]
"""
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])     # Faz append de uma cópia pra não LINKAR os valores da estrutura com a lista
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

turma = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(turma[2][1])
print(turma)
print(turma[1])
print(turma[0][0])
for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dado = list()
for c in range(3):
    dado.append(str(input('Nome: ')).strip().title())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])      # atribui uma cópia dos valores da estrutura dado dentro do indice c de galera
    dado.clear()                # apaga dado
for c in galera:
    print(c[0], c[1])

# EXERCÍCIO 84: Programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
#               [A] Quantas pessoas foram cadastradas       [B] Uma listagem com as pessoas mais pesadas
#               [C] Uma listagem com as pessoas mais leves
# EXERCÍCIO 85: Usuário pode digitar SETE valores numéricos e cadastre-os em uma única lista que mantenha separados os
#               valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
#
# EXERCÍCIO 86: Crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final, imprima a matriz na tela com a
#               formatação correta.
#
# EXERCÍCIO 87: Aprimore o [86] mostrando ao final:
#               [A] A SOMA de todos os valores pares digitados [B] A Soma dos valores da terceira COLUNA
#               [C] O maior valor da segunda LINHA
#
# EXERCÍCIO 88: Programa que ajude um jogador da MEGA SENA a criar palpites. O programa pergunta quantos jogos serão
#               gerados e vai sortear 6 números entre 1 e 60 para cada jogo (sem repetição). Cadastrando tudo em uma
#               lista composta.
#
# EXERCÍCIO 89: Programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
#               mostre um boletim de cada um e permita que o usuário possa mostrar as notas de cada aluno
#               individualmente.    [aluno, [[nota1], [nota2]] ] estrutura com 3 camadas
#
