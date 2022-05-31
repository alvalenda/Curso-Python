# Excercício 25 - Crie um programa se Leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
#
nome = str(input('Nome completo: ')).strip()
corte = nome.title().split()
formatado = ' '.join(corte)

# print(nome, corte, formatado) # REMOVA COMENTÁRIO SE QUISER VER A IMPRESSAO DAS STRINGS
print('ERA só mais um(a) SILVA!!!') if 'Silva' in formatado else print('NÃO era mais um(a) SILVA. =(')
