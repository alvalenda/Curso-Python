# EXERCÍCIOS  40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:  >>> Média abaixo de 5.0: REPROVADO >>> Média entre 5.0 e 6.9:  RECUPERAÇÃO
# >>> Média 7.0 ou superior: APROVADO
while True:
    try:
        n1 = float(input('Primeira nota:\t'))
    except ValueError:
        print('A gente aqui só trabalha com número jovem... NÚMERO!!!')
    else:
        break
while True:
    try:
        n2 = float(input('Segunda nota:\t'))
    except ValueError:
        print('Esqueceu que a entrada precisa ser um número seu arrombado???')
    else:
        break
média = float(n1 * 0.5 + n2 * 0.5)
if média >= 7:
    print('Nota: \033[1;32m{:.2f}\033[m'.format(média))
    print('Situação: \033[1;32mAPROVADO\033[m')
elif média >= 5:
    print('Média: \033[1;34m{:.2f}\033[m'.format(média))
    print('Situação: \033[1;34mRECUPERAÇÃO\033[m')
else:
    print('Nota: \033[1;31m{:.2f}\033[m'.format(média))
    print('Situação: \033[1;31mREPROVADO\033[m')
