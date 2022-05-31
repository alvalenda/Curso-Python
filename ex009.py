# Exercício 9:  Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

''''
    sintaxe da função for em python 3

    for item in range(10):     >>>  varável item faz o loop de 0 a 9 totalizando 10 loops
    print(item)

    for item in range(9, -1, -1):  >>> loop invertido começando em 9, terminando em -1 e com step de -1
    print(item)
    ou seja     >>>     range(start, stop, step)

    Encontrei implementações mais avençadas em: https://www.devmedia.com.br/for-python-estrutura-de-repeticao-for/38513
    Posso guardar o link aqui para futuras aplicações
'''

print('Seja Bem Vindo a Tabuada Maluca 2020!!!')
n:  int
n = int(input('Entre com um número Inteiro: '))

print('*' * 10+'Tabuada do número {}'.format(n)+'*' * 10)

for i in range(20):
    print('{}\tx\t{}\t=\t{}' .format(i + 1, n, n * (i + 1)))
