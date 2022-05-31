# EXERCÍCIO 106: Um minisistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
#                manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
#                OBS.: use menus.
print(f'\033[7m{" CENTRAL DE AJUDA DA VIDA ":#^60}\033[m')
print(f'\033[31;42m{" digite [FIM] para sair ":^60}\033[m')
looping = True
while looping:
    while True:
        print()
        funcao = str(input(f'Ajuda para qual função? ')).strip().lower()
        if bool(funcao):
            if funcao in 'fim':
                looping = False
                quit()
            break
    help(funcao)

