'''
    ==================================================== Aula 23 =======================================================
                                            TRATAMENTO DE ERRO E EXCEÇÕES
                    Como o Python permite tratar erros e criar respostas a essas exceções, aprendendo
                            como usar a estrutura try except no Python de uma forma simples.
    ====================================================================================================================
'''
"""
    ex.: print(x)                       >>> exception == NameError , variável nem existe kkk
    n = int(input('Número: '))
    <<< oito                            >>> exception == ValueError
    a = = int(input('Númerador: '))
    b = = int(input('Denominador: '))
    r = a / b
    se b == 0                           >>> exception == ZeroDivisionError
    2/'2'                               >>> exception == TypeError
    lst = [3, 6, 4]
    print(lst[3])                       >>> exception == IndexError >>> em Dict == KeyError
    import fodase                       >>> exception == ModuleNotFoundError
    Mais uma porrada...
    ************************************[ Toda exceção vem da CLASSE Exception ]***********************************
        try:
            operação
        except:
            falhou
        else:
            sucesso
        finally:
            certo/falha             ### Vai ocorrer em caso de sucesso ou falha, independente.     
    ***************************************************************************************************************
"""
try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Infelizmente você é burro!')
except ZeroDivisionError:
    print(f'Não consegue né Moisés?')
except KeyboardInterrupt:
    print('Usuário, vulgo vc, não informou os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'{r:.1f}')
finally:
    print(f'Arrombaran')

# EXERCÍCIO 113:    Reescreva a função leita_int() que fizemos no ex 104, incluindo agora a possibilidade da digitaçõo
#                   de um número de tipo inválido. Aproveite e crie também uma função leia_float com a mesma
#                   funcionalidade.
#
# EXERCÍCIO 114:    Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
#                   www.pudim.com.br
#
# EXERCÍCIO 115a:   Crie um peque Sistema Modularizado que permita cadastrar pessoas pelo seu nome e idade em um
#                   arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
#                   listar todas as pessoas cadastradas.
#
# EXERCÍCIO 115b:
#
#
# EXERCÍCIO 115c:
#
#
