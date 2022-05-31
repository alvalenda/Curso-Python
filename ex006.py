# Exercício 6:  Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n: float
n = float(input('Entre com um valor numérico: '))
print(type(n))

print('=' * 10 + 'Método 1' + '=' * 10)
print('Número lido:\t\t{:.2f} \nSeu dobro:\t\t\t{:.2f} \nSeu triplo: \t\t{:.2f} \nSua SQRT:\t\t\t{:.2f}' ''
      ''.format(n, 2 * n, 3 * n, pow(n, 0.5)))

# Método dois, armazenando em variáveis
d = t = r = n

d = 2 * d
t = 3 * t
r = r ** 0.5

print('\n' + '=' * 10 + 'Método 2' + '=' * 10)
print('Número lido:\t\t{:.2f} \nSeu dobro:\t\t\t{:.2f} \nSeu triplo: \t\t{:.2f} \nSua SQRT:\t\t\t{:.2f}' ''
      ''.format(n, d, t, r))
