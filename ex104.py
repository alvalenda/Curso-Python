# EXERCÍCIO 104: Crie um programa que tenha a função leia_int(), que vai funcionar de forma semelhante à função
#                input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#                ex.: n = leia_int('Digite um n')
def leia_int():
    global c
    while True:
        try:
            if c > -1:
                num = int(input(f'{c + 1}º número INTEIRO: '))
            else:
                num = int(input(f'Quer ler quantos números inteiros? '))
        except ValueError:
            pass
        else:
            c += 1
            return num


c = int(-1)
lista = []
K = leia_int()
print(f'OK!!!')
for _ in range(K):
    lista.append(leia_int())
print(f'{c} números lidos:', end=' ')
for n in lista:
    print(n, end=' ')
print(f'\nFIM!!!')
