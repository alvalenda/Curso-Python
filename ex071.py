# EXERCÍCIO 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
#               será o valor a ser sacado (número inteiro*) e o programa vai informar quantas cédulas de cada valor
#               serão entregues.    OBS.: Considere que o caixa possui cédulas de RS50, RS20, RS10 e RS1.
from time import sleep
nota_50 = nota_20 = nota_10 = nota_1 = int(0)
print('\033[7m'+'-=*=-' * 5 + ' CAIXA ELETRÔNICO VEROS BANK ' + '-=*=-' * 5 + '\033[m')
while True:
    try:
        saque = abs(int(input('Valor do SAQUE: R$ ')))
    except ValueError:
        print('entrada inválida...')
    else:
        break
saida = saque
if saida // 50 > 0:
    nota_50 = saida // 50
    saida -= (nota_50 * 50)
if saida // 20 > 0:
    nota_20 = saida // 20
    saida -= (nota_20 * 20)
if saida // 10 > 0:
    nota_10 = saida // 10
    saida -= (nota_10 * 10)
if saida > 0:
    nota_1 = saida
    saida -= nota_1
print('Processando...')
sleep(0.8)
print('=' * 45 + '\n\t\t\tRETIRE SEU DINHEIRO\n' + '=' * 45)
sleep(1.5)
if nota_50 > 0:
    print(f'Notas de R$50:\t{nota_50}')
    sleep(0.35)
if nota_20 > 0:
    print(f'Notas de R$20:\t{nota_20}')
    sleep(0.35)
if nota_10 > 0:
    print(f'Notas de R$10:\t{nota_10}')
    sleep(0.35)
if nota_1 > 0:
    print(f'Notas de R$1:\t{nota_1}')
    sleep(0.35)
sleep(0.8)
print('=' * 45)
print(f'\t\tValor do Saque: R${saque:,.2f}')
print('=' * 45)
sleep(0.75)
print('FIM')
