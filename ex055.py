# EXERCÍCIO 55: Programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
#
acu_menor = acu_maior = peso = float(0)
for i in range(5):
    while True:
        try:
            peso = float(input('Entre com o peso da {}ª pessoa: '.format(i + 1)))
        except ValueError:
            print('Precisa ser um número...')
        else:
            break
    if i == 0:
        acu_menor = peso
        acu_maior = peso
    elif peso < acu_menor:
        acu_menor = peso
    elif peso > acu_maior:
        acu_maior = peso
print('Menor peso:\t{:.2f}\nMais forrrrte:\t{:.2f}'.format(acu_menor, acu_maior))
