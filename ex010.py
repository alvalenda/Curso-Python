# Exercício 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
#               comprar.    considere US$1,00==R$5,23

print('Bem Vindo a melhor CASA DE CÂMBIO VIRTUAL DO BRASIL!')
r:  float
d:  float

r = float(input('Qual valor em R$ deverá ser trocado por U$?\t'))

# valor do dóla câmbio hoje
d = 5.23

print('Ok!\nR${:.2f} compra um total de U${:.2f}\nMuito Obrigado!' .format(r, r / d))
