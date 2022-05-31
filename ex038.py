# EXERCÍCIOS  38: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem
# >>> O primeiro valor é maior >>> O segundo valor é maior >>> Não existe valor maior, os dois são iguais.
while True:
    try:
        n1 = int(input('Entre com o Primeiro número inteiro: '))
    except ValueError:
        print('A entrada precisa ser um número inteiro. Tente novamente...')
    else:
        break
while True:  # entrando e testando os dois números
    try:
        n2 = int(input('Entre com o Segundo número inteiro: '))
    except ValueError:
        print('A entrada precisa ser um número inteiro. Tente novamente...')
    else:
        break

if n1 > n2:
    print('O primeiro valor, {}, é o maior.'.format(n1))
elif n1 < n2:
    print('O segundo valor, {}, é o maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais. {} = {}'.format(n1, n2))
