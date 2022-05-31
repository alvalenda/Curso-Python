# EXERCÍCIO 77: Programa que tenha uma tupla com várias palavras. Depois Mostrar para cada palavras quais são as suas
#               vogais.
tulpa = ('Bolo', 'Oleo', 'Palio', 'Vulva', 'Orelha', 'Colostro', 'Augusto', 'Intestino', 'Estrada', 'Sereia', 'Uva')
print('\033[7mIMPRIME AS VOGAIS PRESENTES EM CADA PALAVRA\033[m')
for x in tulpa:
    print(f'Na palavra {x:<9}', end=': ')
    # if 'a' in x or 'A' in x:
    #     print('a', end=', ')
    # if 'e' in x or 'E' in x:
    #     print('e', end=', ')
    # if 'i' in x or 'I' in x:
    #     print('i', end=', ')
    # if 'o' in x or 'O' in x:
    #     print('o', end=', ')
    # if 'u' in x or 'U' in x:
    #     print('u', end='')
    for y in x:
        if y in 'AaEeIiOoUu':
            print(f'{y}', end=' ')
    print('')
