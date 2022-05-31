# EXERCÍCIO 101: Programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
#                de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou
#                OBRIGATÓRIO nas eleições.
def voto(nasc):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - nasc
    if 17 < idade < 60:
        return f'{idade} anos, voto OBRIGATÓRIO.'
    elif idade < 16:
        return f'{idade} anos, voto NEGADO.'
    else:
        return f'{idade} anos, voto OPCIONAL.'


leu = True
while leu:
    try:
        ano_nasc = int(input(f'Ano de Nascimento: '))
    except ValueError:
        pass
    else:
        ano_nasc = abs(ano_nasc)
        print(voto(ano_nasc))
        while True:
            menu = str(input(f'Continuar? ')).strip().upper()
            if bool(menu):
                menu = menu[0]
                if menu in 'S':
                    break
                elif menu in 'N':
                    leu = False
                    break
print(f'FIM!!!')
