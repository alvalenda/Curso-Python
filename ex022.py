# Excercício 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#               *   O nome com todas as letras maiúsculas
#               *   O nome com todas minúsculas
#               *   Quantas letras ao todo (sem considerar espaços)
#               *   Quantas letras tem o primeiro nome
nomes = str(input('Entre com seu nome completo: '))
maius = nomes.upper()
minus = nomes.lower()
corte = nomes.split()
space = nomes.count(' ')

print('Nome:\t\t\t\t\t', nomes)
print('Maiúscula:\t\t\t\t', maius)
print('Minúscula:\t\t\t\t', minus)
print('Título:\t\t\t\t\t', nomes.title())
print('Número de letras:\t\t', len(nomes) - space)
print('Letras primeiro nome:\t', len(corte[0]))
