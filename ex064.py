# EXERCÍCIO 64: Leia vários números inteiros pela teclado. O programa só vai parar quando o usuário digitar 999
#               que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre .
#               eles. Desconsiderando o flag 999
def leitura_int():
    while True:
        try:
            n = int(input('Número Inteiro: '))
        except ValueError:
            print('Número inteiro vai... tenta aí...')
        else:
            global contador
            if n != 999:
                contador += 1
            return n


contador = controle = acumula = 0
while controle != 999:
    print('Entre com um Número inteiro:\t\t[999] SAIR')
    controle = leitura_int()
    if controle != 999:
        acumula += controle
print('Total de números:\t{}\nValores acumulados:\t{}'.format(contador, acumula))
