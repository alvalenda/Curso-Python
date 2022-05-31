import sqlite3
from os import system
from time import sleep
from uteis.dado import leia_int, leia_str
from uteis.menus import *

conecta = sqlite3.connect('cadastro_pessoas.db')    # carrega endereço* do banco de dados
cursor = conecta.cursor()                           # = sqlite3.connect('cadastro_pessoas.db').cursor()
# Cria uma table de banco de dados CASO não exista o arquivo. A tabela contém os elementos "nome" e "idade"
cria_tabela(cursor)
# PROGRAMA PRINCIPAL
while True:
    imp_menu('CADASTRAR NOVA PESSOA',
             'LISTAR PESSOAS CADASTRADAS',
             'SAIR DO PROGRAMA', num=50, titulo='SISTEMA DE CADASTRO 1.0')
    sleep(0.4)
    while True:
        menu = leia_int('O QUE DESEJA FAZER? ', False)
        if menu in [1, 2, 3]:
            print(f'{"*"}' * 50)
            break
    if menu == 1:
        nome = leia_str(f'Qual o NOME do novo usuário? ', 2)[:30]
        idade = leia_int(f'Qual a IDADE do novo usuário? ', False)
        insere_usuario(cursor, conecta, nome, idade)
        sleep(1)
    elif menu == 2:
        mostra_usuario(cursor)
        system("pause")
    elif menu == 3:
        print(f'FINALIZANDO O PROGRAMA')
        break
conecta.close()     # fecha o banco de dados
sleep(1)
print(f'FIM!!!')
