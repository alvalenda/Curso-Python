'''
    ==================================================== Aula 15 =======================================================
                                           INTERROMPENDO REPETIÇÕES - WHILE -
                                   utilizando break para interromper laços infinitos (while)
                                        utilizando as novas fstrings em python
    ====================================================================================================================
'''
"""
            [T]
[][] [] [][][*] [*][][]...

while True:
    if (chão +1) is True:
        anda
    if (chão + 1) is False:
        pula
    if moeda is True:
        pega
    if trofeu is True:
        pula
        pega
        break       # quebra o laço de repetição
"""
n = s = 0
while True:
    n = int(input('Digite um número: [999] para parar'))
    if n == 999:
        break
    s += n
print(f'A soma vale {n}')  # Isso é uma fstring. f seguido de uma string (f'') há uma interpolação  dentro de strings
# que torna possível simplesmente colocar a variável dentro da máscara sem o .format()
# mais exemplos de fstrings
nome = 'Flávio'
idade = 26
print(f'O {nome} tem {idade} anos.')            # 'nova' forma - PEP 498 (fstrings) - PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade))  # PYTHON 3
print('O %s tem %d anos.' % (nome, idade))      # python 2, não recomendado a utilização no 3
salário = 987.35
print(f'O {nome} tem {idade} anos e recebe R${salário:,.2f}.')

# EXERCÍCIO 66: Leia vários números inteiros pela teclado. O programa só vai parar quando o user digitar 999, que é
#               a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# EXERCÍCIO 67: Programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo user.
#               O programa será interrompido quando o número solicitador for negativo.
# EXERCÍCIO 68: Programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER.
#               mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# EXERCÍCIO 69: Programa que leia a idade e o gênero de várias pessoas. A cada pessoa cadastrada o programa deverá
#               perguntar se o usuário quer ou não continuar. No final, mostre: (A) quantas pessoas tem mais de 18 anos
#               (B) quantos homens foram cadastrados. (C) quantas mulheres tem menos de 20 anos.
# EXERCÍCIO 70: Programa que leia nome e preço de vários produtos. O programa deverá perguntar se o usuário vai
#               continuar. No final mostre: (A) Qual é o total gasto na compra. (B) Quantos produtos custam mais
#               de R$1,000.00   (C) Qual é o nome do produto mais barato.
# EXERCÍCIO 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
#               será o valor a ser sacado (número inteiro*) e o programa vai informar quantas cédulas de cada valor
#               serão entregues.    OBS.: Considere que o caixa possui cédulas de RS50, RS20, RS10 e RS1.
