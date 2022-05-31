def aumentar(num=0, inc=0, cifra=False):
    if cifra:
        return moeda(num * (1 + inc * 0.01))
    return num * (1 + inc*0.01)


def diminuir(num=0, dec=0, cifra=False):
    if cifra:
        return moeda(num * (1 - dec*0.01))
    return num * (1 - dec*0.01)


def dobrar(num=0, cifra=False):
    if cifra:
        return moeda(num * 2)
    return num * 2


def metade(num=0, cifra=False):
    if cifra:
        return moeda(num * 0.5)
    return num * 0.5


def moeda(num=0):
    # return f'R$ {num:6.2f}'.replace('.', ',')     # retirei pois com a substuição o retorno vira string
    return f'R$ {num:6,.2f}'


def resumo(num=0, inc=0, dec=0, cifra=True):
    print(f'*' * 55+f'\n{"-~=* RESUMO *=~-".center(53)}\n'+f'*' * 55)
    print(f'\t{f"Um Aumento  de {inc:^2.0f}%:":.<30}.{aumentar(num, inc, cifra):.>15}')
    print(f'\t{f"Uma Redução de {dec:^2.0f}%:":.<30}.{diminuir(num, dec, cifra):.>15}')
    print(f'\t{f"O Drobro  de  {num:^4.1f}:":.<30}.{dobrar(num, cifra):.>15}')
    print(f'\t{f"A Metade  de  {num:^4.1f}:":.<30}.{metade(num, cifra):.>15}')
    print(f'*' * 55 + f'\n' + f'*' * 55)
