# EXERCÍCIO 54: Programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
#               atingiram a maioridade e quantas já são maiores.
from datetime import datetime
hoje = datetime.now()
acu_menor = acu_maior = ano = int(0)
for i in range(7):
    while True:
        try:
            ano = int(input('Ano de nascimento da {}ª pessoa: '.format(i + 1)))
        except ValueError:
            print('Precisa ser um número...')
        else:
            break
    if (hoje.year - ano) < 18:
        acu_menor += 1
    else:
        acu_maior += 1
print('Menores de idade: {}\nMaiores de idade: {}'.format(acu_menor, acu_maior))
