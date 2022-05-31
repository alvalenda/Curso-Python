#  EXERCÍCIO   32: Faça um programa que leia um ano qualquer e mostre se ele Bissexto.
#  Bissexto são divisíveis por 4, exceto os que são múltiplos de 100 sem ser múltiplos de 400
from datetime import date
print('DESCUBRA SE UM ANO FOI, É OU SERÁ \033[1;35;47mBISSEXTO!!!\033[m')
while True:
    try:
        ano = int(input('Entre com um ano: '))
    except ValueError:
        print('Anos são representados por números inteiros, tente novamente...')
    else:
        break
hoje = int(date.today().year)

if ano < hoje:
    tempo = str('foi')
elif ano > hoje:
    tempo = str('será')
else:
    tempo = str('é')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;35m{}\033[m \033[1;32m{}\033[m bissexto!' .format(ano, tempo))
else:
    print('O ano \033[1;35m{}\033[m \033[1;31mnão\033[m {} bissexto. =(' .format(ano, tempo))

if hoje % 4 == 0 and hoje % 100 != 0 or ano % 400 == 0:
    print('Estamos no ano de \033[1;35m{}\033[m e ele \033[1;32mé\033[m bissexto.' .format(hoje))
else:
    print('Estamos no ano de \033[1;35m{}\033[m e ele \033[1;31mnão\033[m é bissexto.' .format(hoje))
