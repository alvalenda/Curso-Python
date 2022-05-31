# EXERCÍCIOS  44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento: >>> à vista dinheiro/cheque: 10% de desconto >>> à vista cartão: 5% desconto >>> em até
# 2x no cartão: preço normal >>> 3x ou mais no cartão: 20% de juros
while True:
    try:
        pbase = float(input('Preço base do produto: R$'))
    except ValueError:
        print('Entre com um valor númerico...')
    else:
        break
print('''
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
while True:
    try:
        menu = int(input('Escolha a forma de pagamento: '))
    except ValueError:
        print('Entre com um número inteiro que faça parte do Menu de opções...')
    else:
        if 1 <= menu <= 4:
            break
        else:
            print('Entre com um número inteiro que faça parte do Menu de opções...')
if menu == 1:
    print('Valor final: R$ {:9,.2f}'.format(pbase * 0.9))
elif menu == 2:
    print('Valor final: R${:9,.2f}'.format(pbase * 0.95))
elif menu == 3:
    print('Valor final: R${:9,.2f}'.format(pbase))
    print('2 x R${:8,.2f}'.format(pbase / 2))
else:
    print('Valor final: R${:9,.2f}'.format(pbase * 1.2))
    for i in range(3, 13):
        print('{}x\tR${:9,.2f}'.format(i, (pbase * 1.2) / i))
