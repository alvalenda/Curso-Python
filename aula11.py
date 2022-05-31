'''
    ==================================================== Aula 11 =======================================================
                                                    CORES NO TERMINAL
                        códigos de escape sequence ANSI para configurar menus para os seus programas
    ====================================================================================================================
'''
'''
Padrão ANSI : escape sequence (Funciona em várias plataformas)
Sintaxe     :       \033[STYLE;TEXT;BACKm (códigos opcionais e podem ser colocados em qualquer ordem)
 ex.:       :       \033[0;33;44m   

STYLE       :   0 - None
                1 - Bold
                4 - Underline
                7 - Negative (inverte tudo)

TEXT        :   30 - Branco
                31 - Vermelho
                32 - Verde
                33 - Amarelo
                34 - Azul
                35 - Magenta
                36 - Ciano
                37 - Cinza (Padrão)
                39 - Estranho

BACK        :   40 - Branco
                41 - Vermelho
                42 - Verde
                43 - Amarelo
                44 - Azul
                45 - Magenta
                46 - Ciano
                47 - Cinza (padrão)

\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[31;42m
\033[m
\033[7;30m
'''
'''
PRÁTICA
'''
print('\033[4;30;45mOlá Mundo!\033[m')
print('\033[1;32;41mOlá Mundo!\033[m')
print('\033[4;36;33mOlá Mundo!\033[m')

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!' .format(3, 5))

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', 'Flávio', '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;37m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], 'Flávio', cores['limpa']))
# DESAFIO
# Fácil: Colocar menus em 10/35 exercícios anteriores
# Master: Colocar menus em 35/35 exercícios
