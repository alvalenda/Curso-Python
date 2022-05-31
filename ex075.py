# EXERCÍCIO 75: Programa que leia 4 valores pelo teclado e guardar numa tupla. Mostre: (A) Quantas vezes apareceu o
#               valor 9 (B) Em que posição foi digitado o primeiro 3 (C) quais foram os números pares.
def ler_float():
    global cont
    while True:
        try:
            n = float(input(f'{cont}º número: '))
        except ValueError:
            print('valor inválido, tente novamente...')
        else:
            cont += 1
            return n


cont = int(1)
print(f'Entre com 4 números:')
tupla = (ler_float(), ler_float(), ler_float(), ler_float())
conta9 = tupla.count(9)
if tupla.count(3) > 0:
    posic3 = tupla.index(3)
else:
    posic3 = -1
print(f'O númnero 9 apareceu um total de {conta9} veze(s)') if conta9 != 0 else print(f'A tupla não contem o número 9')
print(f'O primeiro 3 aparece na {posic3 + 1}ª leitura') if posic3 != -1 else print(f'O número 3 não apareceu na tupla')
print(f'Números pares: ', end='')
for x in tupla:
    if x % 2 == 0:
        print(f'{x:.0f}', end=' ')
