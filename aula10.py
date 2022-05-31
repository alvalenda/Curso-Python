'''
    ==================================================== Aula 10 =======================================================
                                                    CONDIÇÕES: PARTE I
                                   IF, ELSE,CONDIÇÕES SIMPLES, COMPOSTAS E SIMPLIFICADAS
    ====================================================================================================================
'''
'''
INDENTAÇÃO DA ESTRUTRUTURA IF

carro.siga()
if carro.esquerda():          >>> Tudo que é separadado pela tabulação (indentação) está dentro do bloco do if ou else
    carro.sigua()               | 
    carro.direita()             |
    carro.esquerda()            |   CAMINHO VERDE == CAMINHO DE CONDIÇAO TRUE (verdadeiro)
    carro.siga()                |
    carro.direita()             |   
    carro.siga()                |
else:
    carro.siga()                |
    carro.esquerda()            |
    carro.siga()                |   CAMINHO VERMELHO == CAMINHO DA CONDIÇÃO FALSE (falso)
    carro.esquerda()            |
    carro.siga()                |
carro.pare()                  >>> quando a tabulação (indentação) é removida a linha sai do bloco do else.  

ESTRUTURA CONDICIONAL: 
if condição:
    bloco True
else:
    bloco False
    
Exemplo:    
>>> tempo = int(input('Quantos anos tem seu carro?'))
>>> if tempo <= 3:
>>>     print('carro novo')    
>>> else:
>>>     print('carro velho')
>>> print('--FIM--')

CONDIÇÃO SIMPLIFICADA:
>>> tempo = int(input('Quantos anos tem seu carro?'))
>>> print('carro novo' if tempo <= 3 else 'carro velho')
>>> print('--FIM--')
'''
nome = str(input('Qual é o seu nome? '))
if nome.title() == 'Flavio':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!' .format(nome.title()))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) * 0.5
print('Sua média foi {:.2f}' .format(m))
print('Sua média foi boa! PARABÉNS!' if m >= 6.0 else 'Sua média foi ruim! ESTUDE MAIS!')

# EXERCÍCIO   28: Escreve um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o
#                 usuário tentar descobrir qual foi o número escolhido pelo computador
#
# EXERCÍCIO   29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
#                 dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
#
# EXERCÍCIO   30: Crie um programa que leia um número inteiro qualquer e mostra na tela se ele é par um ímpar
#
# EXERCÍCIO   31: Desenvolva um programa que pergunta a distância de uma viagem em KM, calcule o preço da passagem,
#                 cobrando R$0,50 / Km para viagens até 200Km e R$0,45 para viagens mais longas.
#
# EXERCÍCIO   32: Faça um programa que leia um ano qualquer e mostre se ele Bissexto.
#
# EXERCÍCIO   33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#
# EXERCÍCIO   34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#                 Para salários superiores a R$1.250,00, calcule um aumento de 10%;
#                 Para salários inferiores ou iguais, o aumento é de 15%.
#
# EXERCÍCIO   35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ele pode ou não
#                 formar um triângulo.
