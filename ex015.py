# Escreva um programa que pergunte a quantidade de dias que o carro foi alugado e a quantidade de KM que o carro
# percorreu. Calcule o preço a pagar sabendo que o aluguel do carro custa R$60.00/dia e R$0.15/km

dia:    int
km:     float

dia=int(input('Por quantos DIAS o carro ficou alugado?\t'))
km=float(input('Quantos KM o carro rodou neste período?\t'))

print('\nO valor total do aluguel custou R${:.2f}' .format(dia * 60 + km * 0.15))
