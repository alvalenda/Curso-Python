# Exercício 8:  Escreva um programa que leia um valor em metros e o exiba em centímeros e milímetros.

print('Bem Vindo ao conversor de Unidades Metro (m) para Centímetros (cm) e Milímetros(mm)!!!')
m:  float
m = float(input('Entre com um valor em metros: '))

print('Valor em Metros:\t\t\t{:.2f}m \nValor em Centímetros:\t\t{:.2f}cm \nValor em Milímetros:\t\t{:.2f}mm' ''
      '' .format(m, m * 10, m * 1000))
print('Obrigado por utilizar a nossa ferramenta e até a próxima!!!\n[]`s')
