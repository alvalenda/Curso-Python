# EXERCÍCIO 97: Programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e
#               mostre uma mensagem com tamanho adaptável.
from time import sleep


def escreva(txt):
    tam = len(txt) + 8
    print(f'{"="}' * tam)
    print(f'{txt:^{tam}}')
    print(f'{"="}' * tam)


escreva(' TÍTULO: LANCINHO ')
sleep(3)
for i in range(2):
    escreva(' NAMORA, MAS ADORA O PROÍBIDO ')
    sleep(3)
    escreva(' E EU QUE SOU CULPADO, E EU QUE SOU BANDIDO ')
    sleep(3.5)
    escreva(' PREFERE UM ROMANCE ESCONDIDO ')
    sleep(2.8)
    escreva(' SAI NA MADRUGADA PRA DAR LANCINHO COMIGO')
    sleep(3.5)
escreva(' uh uh uh uhUH!!! uh uh uhUhUh!!! uh uh uhUH!!! ')
sleep(13)
escreva(' uh uh uh uhUH!!! uh uh uhUhUh!!! uh uh uhUH!!! ')
sleep(13)
print(f'FIM!!!')

