# Exercício 7:  Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print('Fim do ano letivo\nHora de calcular as médias')
n1:     float
n2:     float
media:  float

n1 = float(input('Entre com a PRIMEIRA NOTA:\t\t'))
n2 = float(input('Entre com a SEGUNDA NOTA:\t\t'))

media = n1*0.5 + n2*0.5

print('\nA média das notas {:.2f} e {:.2f} é:\t{:.2f}' .format(n1, n2, media))
