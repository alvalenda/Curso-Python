# Exercício 11: Faça um programa que leia a largura e a altura de uma parede e em metros, calcule a sua área e a
#               quantidade de tinta necessária para pintá-la. Sabendo que a tinta pinta uma área de 2m²/litro.

print('Calculadora de TINTAS ONLINE!!!')
print('Por gentileza entre com as dimensões (em metros) da Altura e da Largura da parede a ser pintada.')

altura:     float
largura:    float

altura  = float(input('Altura(m): \t'))
largura = float(input('Largura(m):\t'))

print('\nUma parede {:.2f}m x {:.2f}m tem um total de {:.2f}m²' .format(altura, largura, (altura * largura)))
print('Será necessário um total de {:.2f} litro(s) de tinta.' .format(altura * largura * 0.5))
print(' \nSua parede e seu bolso agradecem!!!')
