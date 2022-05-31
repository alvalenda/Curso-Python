# EXERCÍCIO 107: Aula 22
import uteis.dado as dado
import uteis.moeda as mo

num = dado.leia_float('Entre com um número: ')
print(f'Aumento  de  45%: {mo.aumentar(num, 45)}')
print(f'Redução  de  56%: {mo.diminuir(num, 56)}')
print(f'Dobro    de {num}: {mo.dobrar(num)}')
print(f'Metade   de {num}: {mo.metade(num)}')
