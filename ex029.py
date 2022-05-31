# EXERCÍCIO   29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
#                 dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
vel = float(input('Velocidade escalar instantânea do veículo: '))
lim = int(80)
if vel > lim:
    multa = (vel - lim) * 7
    print('Veículo multado com o valor de R${:10,.2f}.' .format(multa))
else:
    print('Veículo dentro dos limites de velocidade.')
    print('Tenha um bom dia! Diriga com segurança.')
