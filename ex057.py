# EXERCÍCIO 57: Leia o gênero de uma pessoa, só aceita M ou F, caso esteja errado peça para digitar
#               novamente até ter um valor correto.
genero = str()
while True:
    try:
        genero = str(input('Gênero (M) ou (F): ')).strip().upper()[0]  # no upper pega apenas a primeira letra
    except ValueError:
        print('Entrada incorreta, tente novamente...')
    if genero in 'FM' and genero != '':     # not in 'fFmM'tb funcionaria se fosse lógica de saída de um while
        break
    else:
        print('Entrada incorreta, tente novamente...')
print('Gênero Feminino.') if genero == 'F' else print('Gênero Masculino.')
