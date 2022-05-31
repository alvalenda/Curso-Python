# EXERCÍCIO 49: Refaça o ex009 mostrando a tabuada de um número que o usuário escolher, só agora
#               utilizando um laço FOR.
from time import perf_counter
print('Seja Bem Vindo a Tabuada Maluca 2020!!!')
n:  int
while True:
    try:
        n = int(input('Entre com um número Inteiro: '))
    except ValueError:
        print('Precisa ser um valor inteiro')
    else:
        break
tac = perf_counter()
print('*' * 10+'Tabuada do número {}'.format(n)+'*' * 10)
for i in range(50):
    print('{}\tx\t{}\t=\t{}' .format(i + 1, n, n * (i + 1)))
tic = perf_counter()
print('\n\n{}s'.format(tic - tac))
