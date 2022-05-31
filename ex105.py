# EXERCÍCIO 105: Uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as
#                seguintes informações: - Quantidade de notas               - A Maior nota           - A Menor nota
#                                       - A Média da turma                  - A Situação(opcional)
#                                       * Adiciona docstrings da função.
from random import random


def notas(*nts, sit=False):
    """
    -> Pega uma sequência com múltiplas notas, trata e retorna um dicionário contendo as informações pedidas
    :param nts: Variável compactada que pode conter múltiplos números float os quais representam notas
    :param sit: sit=True mostra uma situação geral da turma. Relativa a média que é calculada
    :return: Retorna um dicionário que contém valores quantitativos e qualitativos relacionados às notas.
    """
    turma = {'Quantidade': len(nts),
             'Maior': max(nts),
             'Menor': min(nts),
             'Média': sum(nts) / len(nts)
             }
    if sit:
        if turma['Média'] >= 7.5:
            turma['Situação'] = 'Excelente'
        elif turma['Média'] >= 6:
            turma['Situação'] = 'Boa'
        elif turma['Média'] >= 4.5:
            turma['Situação'] = 'Ruim'
        else:
            turma['Situação'] = 'Péssima'
    return turma


resposta = notas(random()*10, random()*10, random()*10, random()*10, random()*10, random()*10, sit=True)
for k, v in resposta.items():
    print(f'{k:<10}: {v:.2f}') if k not in 'Situação' else print(f'{k:<10}: {v}')
