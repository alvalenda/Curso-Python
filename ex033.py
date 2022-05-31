# EXERCÍCIO   33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('\033[35;46m-=-*'*6+'\033[31;46m{( Organizador de Números )}'+'\033[35;46m*-=-'*6+'\033[m')
while True:
    try:
        n1 = float(input('Primeiro número:\t'))
        n2 = float(input('Segundo número: \t'))
        n3 = float(input('Terceiro número:\t'))
    except ValueError:
        print('Entre apenas com números meu amigo. Vai lá, tente novamente...')
    else:
        break
lista = [n1, n2, n3]
lista.sort()
print('\nMétodo 1')
print('Maior:\t{}\nMenor:\t{}' .format(lista[2], lista[0]))  # melhor solução
print('\nMétodo 2')
if n1 > n2 > n3:                                             # solução com IF que fica ENORME
    print('Maior: {}\nMenor: {}' .format(n1, n3))
elif n1 > n3 > n2:
    print('Maior: {}\nMenor: {}' .format(n1, n2))
elif n2 > n1 > n3:
    print('Maior: {}\nMenor: {}' .format(n2, n3))
elif n2 > n3 > n1:
    print('Maior: {}\nMenor: {}' .format(n2, n1))
elif n3 > n2 > n1:
    print('Maior: {}\nMenor: {}' .format(n3, n1))
else:
    print('Maior: {}\nMenor: {}' .format(n3, n2))
