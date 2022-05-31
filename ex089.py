# EXERCÍCIO 89: Programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
#               mostre um boletim de cada um e permita que o usuário possa mostrar as notas de cada aluno
#               individualmente.    [aluno, [[nota1], [nota2]] ] estrutura com 3 camadas
turma = list()
aluno = list()
notas = list()
contador = int(0)
media = float()
print(f'\033[7m=*' * 25 + f'\033[m' + f'\n\033[7m{"NOTAS TURMA 01":^50}\033[m\n' + f'\033[7m=*' * 25 + f'\033[m')
while True:
    while True:
        nome = str(input(f'Nome do {contador + 1}º aluno: ')).strip().title()
        if bool(nome):
            nome = nome[0:30]
            aluno.append(nome)
            break
        else:
            print(f'vazio...')
    for i in range(2):
        while True:
            try:
                n1 = float(input(f'{i + 1}ª nota: '))
            except ValueError:
                print(f'inválido...')
            else:
                notas.append(n1)
                break
    media = (notas[0] + notas[1]) / 2
    notas.append(media)
    aluno.append(notas[:])
    turma.append(aluno[:])
    contador += 1
    aluno.clear()
    notas.clear()
    print(f'{"="}' * 60)
    while True:
        menu = str(input(f'Adicionar Mais Aluno: ')).strip().upper()
        if bool(menu):
            menu = menu[0]
            if menu in 'SN':
                break
    if menu in 'N':
        print(f'{"="}' * 60)
        break
print(f'{"ID":^2}\t{"NOME DO ALUNO":-^30}\t{"NOTA 1":^5}\t{"NOTA 2":^5}\t {"MÉDIA":^5}')
for n, k in enumerate(turma):
    print(f'{n + 1:<3}\t{k[0]:<30}\t{k[1][0]:>5.2f}\t{k[1][1]:>5.2f}\t{k[1][2]:>5.2f}')
print(f'{"="}' * 60)
print(f'Digite o ID do Aluno para ver suas notas. [0] para SAIR')
while True:
    while True:
        try:
            n1 = int(input(f'Ver notas de qual Aluno: '))
        except ValueError:
            print(f'inválido...')
        else:
            if n1 <= len(turma):
                n1 = abs(n1)
                break
    if n1 == 0:
        print(f'{"="}' * 60)
        break
    print(f'{"="}' * 60)
    nota1 = turma[n1 - 1][1][0]
    nota2 = turma[n1 - 1][1][1]
    print(f'Notas de {turma[n1 - 1][0]}: {nota1:.2f} e {nota2:.2f} Média: {(nota1 + nota2)/2:.2f}')
    print(f'{"="}' * 60)
print(f'FIM!!! =)')
