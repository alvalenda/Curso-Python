# Excercício 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a nome "Santo".
cidade = str(input('Entre com o nome da cidade: ')).strip()
corte = cidade.upper().split()

'''Soluçao 1:'''
print('A cidade começa com a cidade Santo.' if corte[0][:5] == 'SANTO' else 'Não há SANTO no primeiro nome da cidade.')

'''Solução 2: '''
# if corte[0].find('SANTO') == -1:
#     print('Não há SANTO no primeiro nome da cidade.')
# else:
#     print('A cidade começa com a cidade Santo.')
print('Forte Abraço!')
