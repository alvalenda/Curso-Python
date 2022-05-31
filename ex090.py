# EXERCÍCIO 90: Programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#               No final mostre o conteúdo da estrutura na tela.
aluno = dict()
turma = list()
while True:
    while True:
        nome = str(input(f'Nome do aluno: ')).strip().title()
        if bool(nome):
            nome = nome[:30]
            break
        else:
            print(f'inválido...')
    while True:
        try:
            media = float(input(f'Média do aluno: '))
        except ValueError:
            print(f'inválido...')
        else:
            media = abs(media)
            break
    aluno['Nome'] = nome
    aluno['Média'] = media
    if aluno['Média'] >= 6:
        aluno['Situação'] = 'Aprovado'
    elif aluno['Média'] < 4:
        aluno['Situação'] = 'Reprovado'
    else:
        aluno['Situação'] = 'Recuperação'
    turma.append(aluno.copy())
    aluno.clear()
    while True:
        menu = str(input(f'Inserir outro aluno? ')).strip().upper()
        if bool(menu):
            menu = menu[0]
            if menu in 'SN':
                break
        else:
            print(f'inválido...')
    if menu in 'N':
        print(f'{" IMPRIMINDO ":#^50}')
        print(f'=' * 50)
        break
con = int(0)
for j in turma:
    for k, v in j.items():
        print(f'{k:<8}: {v:<30}') if k not in 'Média' else print(f'{k:<8}: {v:<30.2f}')
    print(f'=' * 50)
print(f'FIM')
