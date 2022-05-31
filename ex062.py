# EXERCÍCIO 62: Melhore o desafio 061, perguntando para o usuArio se ele quer mostrar mais alguns tremos.
#               O programador encerra quando ele disser que quer mostrar 0 termos.
def leitura_float():
    while True:
        try:
            a = float(input('Valor: '))
        except ValueError:
            print('Entrada inválida. Entre com um número!')
        else:
            return a


print('\033[7mImprime os 10 primeiros termos de uma P.A.\033[m')
print('Entre com o valor do \033[1;31mPRIMEIRO TERMO\033[m da P.A.:')
p1 = float(leitura_float())
print('Entre com o valor da \033[1;31mRAZÃO\033[m da P.A.:')
ra = float(leitura_float())
termo = int(0)
fim = int(10)
while termo < fim:
    tx = p1 + termo * ra
    print('{:,} '.format(tx), end=' ')
    termo += 1
    if termo == fim:
        print('\n{} impressos, deseja visualizar MAIS quantos termos?\t[0] SAIR'.format(termo))
        fim += int(leitura_float())
print('Programa encerrado. {} termos da P.A. foram apresentados'.format(termo))
