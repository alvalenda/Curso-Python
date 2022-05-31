# EXERCÍCIO   34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#                 Para salários superiores a R$1.250,00, calcule um aumento de 10%;
#                 Para salários inferiores ou iguais, o aumento é de 15%.
while True:
    try:
        sal = float(input('Entre com o salário inicial: '))
    except ValueError:
        print('O salário é um número né jovem... vai... tenta de novo...')
    else:
        break
print('\033[32mR${:10,.2f}\033[m' .format(sal))
if sal > 1250:
    sal = sal * 1.1
else:
    sal = sal * 1.15
print('Salário reajustado: \033[35mR${:10,.2f}\033[m' .format(sal))
