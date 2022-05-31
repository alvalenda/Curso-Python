# EXERCÍCIO 76: Programa que tenha uma tupla única com nomes de produtes e seus respectivos preços na sequênia.
#               Mostre uma listagem de preços, organizando os dados em forma tabular
tupla = ('Hamburguer', 15.99, 'X-Burguer', 19.99, 'X-Bacon', 21.99, 'X-Salada', 21.99, 'X-Salada Bacon', 23.99, 'X-Egg',
         21.99, 'X-Egg Bacon', 23.99, 'X-Tudo', 25.99, 'X-Tudão', 29.99, 'Refrigerante', 5.99, 'Água', 3.99)
print('=' * 49 + f'\n{"MENU":^49}' + '\n' + '=' * 49)
for x in range(0, len(tupla), 2):
    print(f'{tupla[x]:.<40}', f'R$ {tupla[x + 1]:>5.2f}')
