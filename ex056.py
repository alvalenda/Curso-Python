# EXERCÍCIO 56: Programa que leia o nome, idade e gênero de 4 pessoas. No final do programa mostre:
#               > A média de idade do grupo. > O nome do Homem mais velho > Quantos mulheres têm menos de 20 anos.
from time import sleep
genero = str('')
idade = idade_old = acu_idade = acu_mulher = int(0)
nome_velho = str('')
for i in range(4):
    print('-'*12, '{}ª Pessoa'.format(i + 1), '-'*12)
    while True:
        try:
            nome = str(input('Nome: ')).strip().title()
        except ValueError:
            print('Precisa ser um nome...')
        else:
            break
    while True:
        try:
            idade = float(input('Idade: '))
        except ValueError:
            print('Precisa ser um número...')
        else:
            break
    while True:
        try:
            genero = str(input('Gênero (F)(M): ')).strip().upper()
        except ValueError:
            print('Digite [M] para masculino ou [F] para feminino')
        if genero == 'F' or genero == 'M':
            break
        else:
            print('Digite [M] para masculino ou [F] para feminino')
    if i == 0:
        acu_idade += idade
        if genero == 'F' and idade < 20:
            acu_mulher += 1
        else:
            idade_old = idade
            nome_velho = nome
    elif idade > idade_old and genero == 'M':
        idade_old = idade
        nome_velho = nome
        acu_idade += idade
    elif genero == 'F' and idade < 20:
        acu_mulher += 1
        acu_idade += idade
    else:
        acu_idade += idade
# print(acu_idade/4, nome_velho, acu_mulher)
sleep(0.5)
print('\n\nMédia da idade do grupo: {}'.format(acu_idade/4))
sleep(0.2)
print('Homem mais velho: {}'.format(nome_velho))
sleep(0.2)
print('Total de mulheres com menos de 20 anos: {}'.format(acu_mulher))
