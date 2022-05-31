# Excercício 26 - Faça um programa que leia uma frase pelo teclado e mostre:
#               *   Quantas vezes aparece a letra "A";
#               *   Em que posição aparece a primeira vez;
#               *   Em que posição ela aparece pela última vez.
frase = str(input('Entre com uma frase: ')).strip().upper()

print('Frase: ', frase.capitalize())
print('Número de caractéres na frase: ', len(frase))
print('Quantidade de letras (A) na frase: ', frase.count('A'))
print('Posição da primeira letra (A): {}' .format(frase.find('A') + 1))
print('Posição da última letra (A): {}' .format(frase.rfind('A') + 1))
