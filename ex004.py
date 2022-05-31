"""
Escrever um programa que mostre o tipo da variável lida e depois teste se ela percetence a várias categorias que
existem dentro da programação. (todas possíveis) (que eu possa conhecer ou descobrir)
A syntax correta de comentários é feita com #, porém descobri que se vc criar uma string de múltiplas linhas o python
irá ignorá-la, pois a linguagem ignora strings não associadas à variáveis. []'s
"""

a = input('Digite uma parada aí: ')

print('\nA variável é to tipo primitivo: {}' .format(type(a)))
print('É somente espaços? {}' .format(a.isspace()))
print('É alfabético? {} ' .format(a.isalpha()))
print('É alphanumérico? {}' .format(a.isalnum()))
print('É numérico? {} ' .format(a.isnumeric()))
print('É inteiro? {}'.format(a.isdigit()))                  # creio que trata-se de um int              (correto)
print('É float? {}' .format(a.isdecimal()))                 # creio que trata-se de um float            (correto)
print('É indentifier? {}' .format(a.isidentifier()))        # checa se pode ser usado cm identidade de uma variável
print('É lowercase? {}' .format(a.islower()))
print('É uppercase? {}' .format(a.isupper()))
print('É capitalizado? {}' .format(a.istitle()))
print('É ascii? {} 1337 sp34k @r0nb4d@n' .format(a.isascii()))
print('É printável? {}' .format(a.isprintable()))
print('Valor booliano: {}' .format(bool(a)))           # converte para lógica booliana     (consegui \o/)
