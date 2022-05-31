'''
    ==================================================== Aula 22 =======================================================
                                                   MÓDULOS E PACOTES
                Como criar módulos em Python e reutilizar nossos códigos em outros projetos. Vamos aprender
                        também como agrupar vários módulos em um pacote, ampliando ainda mais a
                                     modularização em grandes projetos em Python.
    ====================================================================================================================
'''
"""
PQ utilizar módulos???
- Dividir um programa muito grande
- Aumentar a legibilidade
- Organização do código
- Facilitar a manutenção
- Ocultação de código detalhado
- Reutilização em outros projetos
############################################### TEORIA ###############################################
def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1) 


num = int(input(f'Digite um valor: '))
fat = fatorial(num)                     # fatorial não existe de forma explícita em python.
print(f'O fatorial de {num} é {fat}')
-----------------------------------------------------------------------------------------------------------------
Ao modular a gente separa as funções num arquivo .py separado da função principal, podendo ser vários arquivos.
Nesse caso CRIEI um arquivo chamado fatorial.py dentro desse projeto para armazenar funções que são uteis para a 
resolução destes exercícios e dessa aula. 
PARA implementar o módulo basta usar o 'IMPORT' como fizemos com vários outros pacotes.
Criei uma pasta chamada uteis (library) [botão direito na pasta > Mark Past as > Sources Root] >>>
>>> Isso torna a pasta raiz para códigos de módulos pro projeto.
A partir de agora posso colocar arquivos ali com funções e métodos para todo o projeto e importar.
Esse é o conceito básico de modularização 
-----------------------------------------------------------------------------------------------------------------
Quando o módulo fica MUITO cheio de funções/métodos se faz necessário separá-lo em vários módulos menores criando
um PACOTE. 
PACOTE = Uma pasta que contém MÓDULOS   (podendo ser organizado por assuntos se quiser)
Dentro da pasta uteis por exemplo:
uteis > números.py contém funções para o tratamento de números
uteis > strings.py contém funções para o tratamento de strings
uteis > datas.py contém funções compatíveis com datas
uteis > menus.py contém funções pra manupular menus
etc...
'import uteis' pega TODOS
'from uteis import datas'
--------------------------------------------- PARA CRIAR UM PACOTE ---------------------------------------------
Todo arquivo .py é potencialmente um módulo e toda pasta potencialmente é um pacote
então criaremos essa estrutura aqui no projeto
:uteis:
    :menus:
    :datas:
    :numeros:
    :strings:
dentro de cada uma dessas pasta precisa ter o arquivo __init__.py
o pycharm já faz isso pra vc quando vc cria um pacote
botão direito no projeto >>> NEW >>> Python Package
dentro do pacote uteis>>numeros abrir o arquivo __init__.py e colocar as funções lá
no caso a função FATORIAL.
OU SEJA:
fatorial() é uma função do pacote uteis que está dentro de numeros
import uteis
ou from uteis import numeros
(* Tive um problema que marcava as 'uteis' e 'numeros' abaixo no código
    mas resolvi marcando a parta 'Curso' como a Root do código fonte. O que faz sentido!
    parece que assim ele procura uteis dentro de Curso e numeros dentro de uteis como deveria
    ser feito* )

"""
from uteis.numeros import fatorial

num = int(input(f'Digite um valor: '))
fat = fatorial(num)  # fatorial não existe de forma explícita em python.
print(f'O fatorial de {num} é {fat}')

# EXERCÍCIO 107: Crie o módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobrar() e
#                metade(). Depois faça um programa que importe esse módulo e use algumas dessas funções.
#                aumentar e reduzir é x% em cima de um valor passado.
#
# EXERCÍCIO 108: Adapte o código do desafio 107, criando uma função adicional chamda moeda() que consiga mostrar os
#                valores como um valor monetário formatado.
#
# EXERCÍCIO 109: Modifique as funções que foram criadas no 107 para que eles aceitem um parâmetro a mais, informando
#                se o valor retornado por eles vai ser ou não formatado pela função moeda(), desenvolvida no 108.
#
# EXERCÍCIO 110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre
#                na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
#
# EXERCÍCIO 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
#                Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha
#                tudo funcionando.
#
# EXERCÍCIO 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Cria uma
#                função chamada leia_dinheiro() que seja capaz de funcionar como a função input() mas com uma
#                validação de dados para aceitar apenas valores que sejam monetários.
#
