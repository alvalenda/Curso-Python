# EXERCÍCIO 65: Leia vários números inteiros pelo teclado. No final mostre a média entre todos os valores e qual foi o
#               maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
#               digitar valores.
def leitura_int():
    while True:
        try:
            n = int(input('Número Inteiro: '))
        except ValueError:
            print('Número inteiro vai... tenta aí...')
        else:
            global contador, maior, menor
            if contador == 0:
                maior = menor = n
            elif n > maior:
                maior = n
            elif n < menor:
                menor = n
            contador += 1
            return n


contador = maior = menor = acumula = numero = 0
controle = str('S')
print('Entre com um Número inteiro:')
while controle not in 'nN':
    numero = leitura_int()
    acumula += numero
    if contador % 5 == 0:
        while True:
            try:
                controle = str(input('Deseja continuar a digitar valores [S][N]: ')).strip().upper()
            except ValueError:
                print('opção inválida...')
            if controle not in '':
                controle = controle[0]
            if controle in 'SN' and controle not in '':
                break
print('Total de números:\t{}\nMédia dos valores:\t{}'.format(contador, acumula / contador))
print('Maior número:\t{}\nMenor número:\t{}'.format(maior, menor))
