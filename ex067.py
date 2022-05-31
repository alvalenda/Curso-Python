# EXERCÍCIO 67: Programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo user.
#               O programa será interrompido quando o número solicitador for negativo.
from time import sleep
print('\033[7mSUPER TABUADA 2000\033[m')
while True:
    print('Entre com um número negativo para sair')
    while True:
        try:
            num = int(input('Tabuada do Número: '))
        except ValueError:
            print('entrada inválida...')
        else:
            break
    if num < 0:
        break
    print('-=*='*20)
    for i in range(20):
        print(f'{num} x {i + 1} = {num * (i + 1)}')
        sleep(0.1)
    print('-=*=' * 20)
    sleep(1)
print('FIM :)')
