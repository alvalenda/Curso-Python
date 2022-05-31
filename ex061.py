# EXERCÍCIO 61: Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os
#               10, primeiros termos da progressão usando a estrutura while.
def leitura_float():
    while True:
        try:
            a = float(input('Valor: '))
        except ValueError:
            print('Entrada inválida. Entre com um número!')
        else:
            return a


print('\033[7mImprime os 10 primeiros termos de uma P.A.\033[m')
print('Entre com o valor do PRIMEIRO TERMO da P.A.:')
p1 = float(leitura_float())
print('Entre com o valor da RAZÃO da P.A.:')
ra = float(leitura_float())
termo = int(0)
while termo < 10:
    tx = p1 + termo * ra
    print('{:,.2f} '.format(tx), end=' ')
    termo += 1
