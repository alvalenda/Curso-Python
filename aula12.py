'''
    ==================================================== Aula 12 =======================================================
                                                  CONDIÇÕES: PARTE II
                                            CONDIÇÕES ANINHADAS: IF... ELIF
    ====================================================================================================================
'''
"""
if carro.esquerda():
    bloco 1
elif carro direita()    >>> ELSE IF = ELIF (pode ter quantos elis quiser e só um ou nenhum else)
    bloco 2
else:
    bloco3
    
    era só isso mesmo... agora é exercício e exemplo. 
"""
nome = str(input('Qual é seu nome? ')).strip().title()
if nome == 'Flavio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Júlia Vitória':
    print('Nossa gata! Que nome mais delícia.')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!' .format(nome))

# EXERCÍCIOS  36: Crie um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e sem quantos anos ele vai pagar.Calcule o valor da
# prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empr será negado.
#
# EXERCÍCIOS  37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversão: >>> 1 para binário >>> 2 para octal e >>> 3 para hexadecimal
#
# EXERCÍCIOS  38: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem
# >>> O primeiro valor é maior >>> O segundo valor é maior >>> Não existe valor maior, os dois são iguais.
#
# EXERCÍCIOS  39: Faça um programq que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# >>> Se ele ainda vai se alistar ao serviço militar. >>> Se é a hora de se alistar >>> Se já passou o tempo de
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#
# EXERCÍCIOS  40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:  >>> Média abaixo de 5.0: REPROVADO >>> Média entre 5.0 e 6.9:  RECUPERAÇÃO
# >>> Média 7.0 ou superior: APROVADO
#
# EXERCÍCIOS  41: A Conferação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade: >>> até 9 anos: MIRIM >>> 14 anos: INFANTIL >>>
# 19 anos: JUNIOR >>> 20 anos: SÊNIOR >>> acima: MASTER
#
# EXERCÍCIOS  42: Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado: >>> Equilátero: (todos os lados iguais) >>> Isósceles: Dois lados iguais >>> Escaleno: Todos os
# lados diferentes
#
# EXERCÍCIOS  43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo: >>> abaixo de 18.5: Abaixo do Peso >>> Entre 18.5 e 25: Peso Ideal >>>
# 25 até 30: Sobrepeso >>> 30 até 40: Obesidade >>> Acima de 40: Obesidade mórbida
#
# EXERCÍCIOS  44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento: >>> à vista dinheiro/cheque: 10% de desconto >>> à vista cartão: 5% desconto >>> em até
# 2x no cartão: preço normal >>> 3x ou mais no cartão: 20% de juros
#
# EXERCÍCIOS  45: Crie um programa que faça o computador jogar Jokenpô com você. >>> Pedra >>> Papel >>> Tesoura
