def imp_menu(*opcoes, num=50, titulo=' Menu do Programa '):
    print(f'*' * num)
    print(f'{ titulo }'.center(num))
    print(f'*' * num)
    c = int(0)
    for i in opcoes:
        print(f'\t:{(c + 1):^3}:  {i:.<{num - 15}}')
        c += 1
    # print(f'\t:{2:^3}:  {"LISTAR PESSOAS CADASTRADAS":.<{num - 15}}')
    # print(f'\t:{3:^3}:  {"SAIR DO PROGRAMA":.<{num - 15}} ')
    print(f'*' * num)


def mostra_usuario(cursor):
    cursor.execute('''
        SELECT nome, idade FROM users;
    ''')
    print(f'\t{"IMPRIMINDO LISTA DE USUÁRIOS"::^35}\n')
    for n, i in cursor.fetchall():
        print(f'\t{n:<30}\t{i:<3} anos')
    print(f'\n\t{"LISTA IMPRESSA COM SUCESSO"::^35}')


def insere_usuario(cursor, conn, nome, idade):
    cursor.execute(f'''
        INSERT INTO users (nome, idade)
        VALUES ('{nome}', '{idade}')
    ''')
    conn.commit()   # salva as alterações no banco de dados passado
    print(f'{" usuário cadastrado com SUCESSO! "::^35}')


def cria_tabela(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        nome TEXT NOT NULL,
        idade TEXT NOT NULL
    );
    ''')
