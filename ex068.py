# EXERCÍCIO 68: Programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER.
#               mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep
print('\033[7mPAR OU ÍMPAR!!!!\033[m')
vitoria = int(0)
while True:
    print('=*=' * 20)
    while True:
        try:
            jogador_pi = str(input('PAR ou ÍMPAR? [P][I] ')).strip().upper()
        except ValueError:
            print('Opção inválida...')
        else:
            if jogador_pi.isalnum():
                if jogador_pi[0] in 'PIÍ':
                    jogador_pi = jogador_pi[0]
                    break
                else:
                    print('opção inválida...')
            else:
                print('vazio, opção inválida...')
    while True:
        try:
            jogador_num = int(input('Coloque o Número: '))
        except ValueError:
            print('opção inválida')
        else:
            break
    pc_num = randint(0, 5)
    resultado = int(jogador_num + pc_num)
    sleep(0.8)
    if jogador_pi in 'P':
        if resultado % 2 == 0:
            print(f'Meu número: {pc_num}\nSeu número: {jogador_num}\n{resultado} é PAR!!! =)\nParabéns!!! ')
            vitoria += 1
            sleep(0.5)
        else:
            print(f'Meu número: {pc_num}\nSeu número: {jogador_num}\n{resultado} é ÍMPAR!!! kkk\nErrrrrou!!!')
            sleep(0.5)
            break
    else:
        if resultado % 2 == 1:
            print(f'Meu número: {pc_num}\nSeu número: {jogador_num}\n{resultado} é ÍMPAR!!! =)\nParabéns!!!')
            vitoria += 1
            sleep(0.5)
        else:
            print(f'Meu número: {pc_num}\nSeu número: {jogador_num}\n{resultado} é ÍMPAR!!! kkk\nErrrrrou!!!')
            sleep(0.5)
            break
print('=*=' * 20)
sleep(0.5)
print(f'DOIDERA!!! Você teve {vitoria} vitória(s) consecutivas!!!')
