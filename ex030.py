# EXERCÍCIO   30: Crie um programa que leia um número inteiro qualquer e mostra na tela se ele é par um ímpar
#
entrada = ' '
while entrada.isnumeric() is False:
    entrada = str(input('Entre com um número inteiro: '))

entrada = int(entrada)

if entrada % 2 == 0:
    print('{} é \033[1;35mPAR.' .format(entrada))
else:
    print('{} é \033[1;34mÍMPAR.' .format(entrada))
