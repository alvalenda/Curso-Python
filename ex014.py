# Escreva um programa que leia uma temperatura em graus celsius e converta para fahrenheit

print('Conversor de temperatura.\nConverte Celsius para Fahrenheit')

tempc:  float
tempf:  float
tempc = float(input('Digite temperatura em Celsius:\t'))
tempf = (tempc * 9/5) + 32

print('{:.1f}°C equivalem a {:.1f}°F'.format(tempc, tempf))
