# EXERCÍCIOS  41: A Conferação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade: >>> até 9 anos: MIRIM >>> 14 anos: INFANTIL >>>
# 19 anos: JUNIOR >>> 20 anos: SÊNIOR >>> acima: MASTER
from datetime import datetime
print('\033[1;30;46m=*'*5+'\033[1;31;46m < CONFEDERAÇÃO NACIONAL DE NATAÇÃO > '+'\033[1;30;46m*='*5+'\033[m')
while True:
    try:
        ano = int(input('Ano de nascimento do atleta: '))
    except ValueError:
        print('Entre com um número inteiro.')
    else:
        break
idade = int(datetime.now().year - ano)
if idade <= 9:
    print('Idade:\t\t{} anos'.format(idade)+'\nCategoria:\tMIRIM')
elif idade <= 14:
    print('Idade:\t\t{} anos'.format(idade)+'\nCategoria:\tINFANTIL')
elif idade <= 18:
    print('Idade:\t\t{} anos'.format(idade)+'\nCategoria:\tJUNIOR')
elif idade <= 23:
    print('Idade:\t\t{} anos'.format(idade)+'\nCategoria:\tSÊNIOR')
else:
    print('Idade:\t\t{} anos'.format(idade)+'\nCategoria:\tMASTER')
