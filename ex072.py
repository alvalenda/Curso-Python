# EXERCÍCIO 72: Programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#               O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze'
         , 'Quatorze', 'Quinze', 'Dezesses', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        try:
            num = int(input('Entre com um número de 0 a 20: '))
        except ValueError:
            print(f'valor inválido...')
        else:
            if 0 <= num <= 20:
                break
            else:
                print(f'precisa ser um valor entre 0 e 20 seu imbecil...')
    print(f'Você digitou o número {tupla[num]}')
    # for x, y in enumerate(tupla):
    #     print(x, y)
    while True:
        menu = str(input('Deseja digitar mais números? [S][N] ')).strip().upper()
        if menu not in '':
            menu = menu[0]
            if menu in 'SN':
                break
        else:
            print('valor inválido, tente novamente...')
    if menu in 'N':
        break
print('FIM ;)')
