'''
    ==================================================== Aula 21 =======================================================
                                                    FUNÇÕES (PARTE ii)
                Mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções,
                    argumentos opcionais para dar mais dinamismo em funções Python, escopo de
                                            variáveis e retorno de resultados.
    ====================================================================================================================
'''
"""
        ----------------------- ITERACTIVE HELP -------------------------
para obter uma ajuda iterativa basta usar help()
help()
apos chamar a função help vc tem acesso a ajuda e documentação sobre funcionalidades do python
help(print)
ou entrar no console do python digitar help() e lá buscar ajuda sobre qqer coisa.

print(input.__doc__) imprime a documentação do input (uma outra forma de conseguir a ajuda)

        -------------------------- DOCSTRINGS ----------------------------
Docstrings são strings de documentação como as que vc recebe acessando o help ou __doc__ nos casos acima.
exemplo:
def contador(i, f, p):
"""   # Ao abrir apas triplas na linha abaixo da definição da função vc cria a docstring da função
# -> Faz uma contagem e mostra na tela.
# :param i: início da contagem
# :param f: fim da contagem
# :param p: passo da contatgem
# :return: sem retorno
"""         # Lembrar que as áspas triplas e a docstring precisa estar indentado corretmente dentro da def
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c+=p
    print('FIM!')
    
help(contador)

        -------------------------- PARÂMETROS OPCIONAIS ----------------------------
def somar(a, b, c=0):
    s = a + b + c
    print(f'{s}')
    
    
somar(3, 2, 5)
somar(8, 4)     # como c recebe ZERO na def ele se torna paraâmetro opcional
Nada me impede de colocar todas = 0

        -------------------------- ESCOPO DE VARIÁVEIS ----------------------------
Onde a variável existe.
def teste():
    x = 8
    print(f'{n}')   >>>     2
    print(f'{x}')   >>>     8
    
    
n = 2
print(f'{n}')   >>>     2
print(f'{x}')   >>>     ERRO

n é uma variável global
x é uma variável local válida dentro de teste()
se 'n' for declarada dentro da função com outro valor, ele não altera o valor de 'n' global
ele cria uma versão local de n. 
Para alterar 'n' dentro da função ele precisa ser declarado como 'global n', aí vai se tratar da mesma variável global

Também existe escopo de chamada de biblioteca, pode tornar o método local ou global

        -------------------------- RETORNANDO VALORES ----------------------------
usando return n a função retorna n  -> FIM! =)
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

soma1 = somar(1, 2, 3)
soma2 = somar(1, 2)
soma3 = somar(0)
print(f'{soma1}')       >>>     6
print(f'{soma1}')       >>>     3
print(f'{soma1}')       >>>     0

"""


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'{s}')


somar(3, 2, 5)
somar(8, 4)  # como c recebe ZERO na def ele se torna paraâmetro opcional
somar(c=3, a=2)
somar(a=1)
print()


def fatorial(num=1):                    # calcula o fatorial de um número
    if num == 1 or num == 0:
        return 1
    return num * fatorial(num - 1)


for n in range(11):
    print(f'{n:<2}! = {fatorial(n):>8}')

# EXERCÍCIO 101: Programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
#                de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou
#                OBRIGATÓRIO nas eleições.
#
# EXERCÍCIO 102: Programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indicará o número
#                a calcular e o outro chamado show, que será o valor lógico (opcional) indicando se será mostrado ou
#                não na tela o precesso de cálculo do fatorial.
#
# EXERCÍCIO 103: Uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos
#                gols ele marcou. Deverá ser capaz de mostrar a ficha do jogador, mesmo que não tenha sido informado
#                corretamente.
#
# EXERCÍCIO 104: Crie um programa que tenha a função leia_int(), que vai funcionar de forma semelhante à função
#                input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#                ex.: n = leia_int('Digite um n')
#
# EXERCÍCIO 105: Uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as
#                seguintes informações: - Quantidade de notas       - A Maior nota          - A Menor nota
#                                       - A Média da turma          - A Situação (opcional)
#                                       * Adiciona docstrings da função.
#
# EXERCÍCIO 106: Um minisistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
#                manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
#                OBS.: use menus.
#
