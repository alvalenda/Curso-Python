# EXERCÍCIO   28: Escreve um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o
#                 usuário tentar descobrir qual foi o número escolhido pelo computador
from random import randint
from time import sleep
k = int(5)
j = float(1/k * 100)
contador = [0, 0, 0, 0, 0, 0]
acerto = errou = int(0)
print('-=*=-'*20)
print('\t\t\t\t\tVou pensar num número entre 0 e 5. Tente acertar...')
print('-=*=-'*20)
for i in range(k):
    num = randint(0, 5)
    contador[num] += 1
    entrada = int(input('Em que número eu pensei? '))
    sleep(0.8)
    if entrada == num:
        print('Parabéns! Acertou! Era o número {}.' .format(num))
        acerto += 1
    else:
        print('ERRRRRRRROU!!! Era o número {}.' .format(num))
        errou += 1

print('Distribuição de ocorrência dos números e taxa de acerto.\n\t\t\t\t', contador)
print('processando...')
sleep(2)
print('0:\t{:.2f}%\n1:\t{:.2f}%\n2:\t{:.2f}%\n3:\t{:.2f}%\n4:\t{:.2f}%\n5:\t{:.2f}%' ""
      "" .format(contador[0] * j, contador[1] * j, contador[2] * j, contador[3] * j, contador[4] * j, contador[5] * j))
sleep(1)
print('Acertou:\t{}%' .format(acerto * j))
print('Errou:\t\t{}%'.format(errou * j))
