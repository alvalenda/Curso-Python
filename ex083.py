# EXERCÍCIO 83: Programa em que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
#               analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#               (creio que seja só contar os parênteses abertos e fechados e a ordem '(' antes de ')' )
buff_cha = buff_col = buffer = pos = int(0)
fail = bool(False)
while True:
    expre = str(input('Entre com uma Expressão Matemática: ')).strip()
    if bool(expre):
        if ('(' in expre) or ('[' in expre) or ('{' in expre) or (')' in expre) or (']' in expre) or ('}' in expre):
            break
        else:
            print('expressão inválida')
    else:
        print('vazio')
for i in expre:
    if i in '(':
        buffer += 1
    elif i in ')':
        buffer -= 1
    elif i in '[':
        buff_col += 1
    elif i in ']':
        buff_col -= 1
    elif i in '{':
        buff_cha += 1
    elif i in '}':
        buff_cha -= 1
    if buffer < 0:
        print(f'\033[7mExpressão INVÁLIDA!!!\033[m\nFechou de forma equivocada no {pos + 1}º elemento da expressão.')
        for j in range(len(expre)):
            if j == pos:
                print(f'\033[7m', end='')
            print(f'{expre[j]}', end='')
            if j == pos:
                print(f'\033[m', end='')
        print('')
        fail = True
        break
    elif buff_col < 0:
        print(f'\033[7mExpressão INVÁLIDA!!!\033[m\nFechou de forma equivocada no {pos + 1}º elemento da expressão.')
        for j in range(len(expre)):
            if j == pos:
                print(f'\033[7m', end='')
            print(f'{expre[j]}', end='')
            if j == pos:
                print(f'\033[m', end='')
        fail = True
        print('')
        break
    elif buff_cha < 0:
        print(f'\033[7mExpressão INVÁLIDA!!!\033[m\nFechou de forma equivocada no {pos + 1}º elemento da expressão.')
        for j in range(len(expre)):
            if j == pos:
                print(f'\033[7m', end='')
            print(f'{expre[j]}', end='')
            if j == pos:
                print(f'\033[m', end='')
        fail = True
        print('')
        break
    pos += 1
if (buffer > 0 or buff_cha > 0 or buff_col > 0) and not fail:
    print(f'\033[7mExpressão INVÁLIDA!!!\033[m')
    if buffer == 1:
        print(f'Faltando fechar {abs(buffer)} parêntese')
    if buff_col == 1:
        print(f'Faltando fechar {abs(buff_col)} colchete')
    if buff_cha == 1:
        print(f'Faltando fechar {abs(buff_cha)} chave')
    if buffer > 1:
        print(f'Faltando fechar {abs(buffer)} parênteses')
    if buff_col > 1:
        print(f'Faltando fechar {abs(buff_col)} colchetes')
    if buff_cha > 1:
        print(f'Faltando fechar {abs(buff_cha)} chaves')
elif buffer == buff_col == buff_cha == 0:
    print(f'\033[7mExpressão VÁLIDA!!!\033[m')
print(f'\nFIM\n=)')
