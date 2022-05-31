# EXERCÍCIO 58: Melhorar o jogo do desafio 028 onde o computador vai "pensar" um número entre 0 e 10.
#               Agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
#               dados até conseguir 'vencer'. kkk
from random import randint
from time import sleep
acerto = palpites = int(0)
print('\033[7m-=*=-'*20, '\033[m')
print('\033[7m\t\t\t\t\tVou pensar num número entre 0 e 10. Tente acertar...\t\t\t\t\t\t\t', '\033[m')
print('\033[7m-=*=-'*20, '\033[m')
num = randint(0, 10)
entrada = int(-1)
while entrada != num:
    entrada = int(input('Em que número eu pensei? '))
    sleep(0.5)
    if entrada == num:
        print('Parabéns! Acertou! Era o número {}.' .format(num))
        palpites += 1
        acerto += 1
    elif abs(entrada - num) == 2:
        print('\033[1;31m ihhhhhhh Tá Quente!!!\033[m')
        palpites += 1
    elif abs(entrada - num) == 1:
        print('\033[1;31m TÁ PEGANDO FOGO BICHO!!!!!!\033[m')
        palpites += 1
    elif abs(entrada - num) <= 4:
        print('Tá morno...')
        palpites += 1
    elif abs(entrada - num) <= 6:
        print('\033[1;34m Tá friooooo friooooo friozinho inho zinho frioinho\033[m')
        palpites += 1
    elif abs(entrada - num) <= 8:
        print('\033[1;34m Tá muito frio... MUITO FRIO...\033[m')
        palpites += 1
    else:
        print('\033[1;34m TÁ CONGELADO IRMÃO!\033[m')
        palpites += 1
j = float(1 / palpites * 100)
print('Foram necessários {} palpites para acertar.\t\t\t\t'.format(palpites))
print('processando...')
sleep(1)
print('Acertou:\t{:.2f}%' .format(acerto * j))
print('Errou:\t\t{:.2f}%'.format((palpites - acerto) * j))
