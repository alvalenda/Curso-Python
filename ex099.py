# EXERCÍCIO 99: Programa que tenha uma função chamada maior(), que receba várias parâmetros com valores inteiros.
#               O programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(var):
    ma = var[0]
    for n in var:
        if n > ma:
            ma = n
    return ma


numeros = tuple()
while True:
    try:
        ene = int(input(f'DESEJA LER QUANTOS NÚMEROS INTEIROS? '))
    except ValueError:
        pass
    else:
        ene = abs(ene)
        break
for x in range(ene):
    while True:
        try:
            num = (int(input(f'{x +1}º NÚMERO: ')),)    # O (bla, ) torna num em uma tupla
        except ValueError:
            pass
        else:
            numeros += num                              # Sendo uma tupla ele pode ser concatenado com numeros
            del num                                     # deleta pra poder ser relida no for
            break
print(f'O MAIOR VALOR DIGITADO FOI: {maior(numeros)}')
