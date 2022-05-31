def leia_float(msg='Número float: ', negativo=True):
    while True:
        try:
            n = float(input(f'{msg}'))
        except ValueError:
            pass
        else:
            if not negativo:
                n = abs(n)
            return n


def leia_int(msg='Número inteiro: ', negativo=True):
    while True:
        try:
            n = int(input(f'{msg}'))
        except ValueError:
            pass
        else:
            if not negativo:
                n = abs(n)
            return n


def leia_str(msg='Valor da String: ', formato=0):
    """
    -> Função básica para Ler uma STRING via teclado do usuário.
    :param msg: Mensagem que será impressa na tela ao pedir a leitura da string
    :param formato: Formatações especiais. 0 = Não, 1 = .upper, 2 = .title, 3 = .lower
    :return: Retorna uma STRING lida no teclado sempre com o tratamento .strip
    """
    while True:
        if formato == 1:
            n = str(input(f'{msg}')).strip().upper()
        elif formato == 2:
            n = str(input(f'{msg}')).strip().title()
        elif formato == 3:
            n = str(input(f'{msg}')).strip().lower()
        else:
            n = str(input(f'{msg}')).strip()
        if bool(n):
            return n


def leia_moeda(msg='Valor em R$: '):
    while True:
        n = str(input(f'{msg}')).strip()                        # solução que troca apenas uma vírgula
        # n = str(input(f'{msg}')).strip().replace(',', '.')    # solução melhorada
        if bool(n):
            if ',' in n:
                a = n.find(',')     # a é a posição da vírgula na string
                b = n[:a]           # b acumula os valores de todos os dígitos até a ',' exceto a vírgula
                c = n[a+1:]         # c acumula os valores posterioes a ',' podendo ser vazio sem problemas
                n = b[:] + '.' + c  # n é igual aos valores pré ',' + um '.' substituindo vírgula + valores pós ','
            try:
                return float(n)
            except ValueError:
                print(f'entrada inválida')
                # pass
