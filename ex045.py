# EXERCÍCIOS  45: Crie um programa que faça o computador jogar Jokenpô com você. >>> Pedra >>> Papel >>> Tesoura
from random import choice
from time import sleep
maquina = ['Pedra', 'Papel', 'Tesoura']
placar = {'Vitória': 0,
          'Empate ': 0,
          'Derrota': 0}
print('\033[7m'+'-=*='*10+'!!! JOKENPO BRASIL !!!'+'-=*='*10+'\033[m')
print('Digite:\t\033[1;36mSair\033[m - Para fechar o jogo\n\t\t\033[1;36mPlacar\033[m - Para imprimir o placar.')

while True:
    try:
        jogador = str(input('Pedra, Papel ou Tesoura?\t')).strip().title()
    except ValueError:
        print('Digite uma das opções viáveis para o jogo jovem...')
    else:
        if jogador == 'Sair':
            break
        elif jogador == 'Placar':
            for x, y in placar.items():
                print(x, y)
        else:
            print('JO', end='-')
            sleep(0.45)
            print('KEN', end='-')
            sleep(0.45)
            print('PO!!!!')
            sleep(0.2)
            escolha = choice(maquina)
            if jogador == escolha:
                print('EMPATOU!!!\t{} empata com {}!!!'.format(jogador, escolha))
                placar['Empate '] += 1
            elif jogador == 'Pedra' and escolha == 'Papel':
                print('PERDEU!!!\tA {} perde para o {}!!!'.format(jogador, escolha))
                placar['Derrota'] += 1
            elif jogador == 'Pedra' and escolha == 'Tesoura':
                print('VITÓRIA!!!\tA {} vence a {}!!!'.format(jogador, escolha))
                placar['Vitória'] += 1
            elif jogador == 'Papel' and escolha == 'Pedra':
                print('VITÓRIA!!!\tO {} vence a {}!!!'.format(jogador, escolha))
                placar['Vitória'] += 1
            elif jogador == 'Papel' and escolha == 'Tesoura':
                print('PERDEU!!!\tO {} perde para a {}!!!'.format(jogador, escolha))
                placar['Derrota'] += 1
            elif jogador == 'Tesoura' and escolha == 'Pedra':
                print('PERDEU!!!\tA {} perde para a {}!!!'.format(jogador, escolha))
                placar['Derrota'] += 1
            elif jogador == 'Tesoura' and escolha == 'Papel':
                print('VITÓRIA!!!\tA {} vence o {}!!!'.format(jogador, escolha))
                placar['Vitória'] += 1
            else:
                print('{} não é uma opção válida.'.format(jogador))
