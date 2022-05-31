# Exercício 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. ggez

print('O Mercado 7 Anões está LOUCO!!!\nTudo com 5% de desconto!!!')
p:  float

p = float(input('Entre com o valor do produto:\t'))

print('O valor do produto com o desconto aplicado é de R${:.2f}' .format(p * 0.95))
