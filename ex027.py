# Excercício 27 - Faça um programa que leia o nome completo de uma pessoa, mostre em seguida o primeiro e o último nome
#                 separadamente. ex.: Ana Maria Braga Coxta Marota >>> Ana Marota.
listanome = str('')
while bool(listanome) is False:
    nome = str(input('Nome Completo: ')).strip().title()
    listanome = nome.split()

tamanho = int(len(listanome))
print('Senhor(a): {} {}' .format(listanome[0], listanome[tamanho - 1]))
