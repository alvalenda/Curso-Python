# EXERCÍCIO 53: Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando
#               os espaços.     ex.: 'APOS A SOPA' 'A SACADA DA CASA' 'A TORRE DA DERROTA' ''O LOBO AMA O BOLO'
#               'ANOTARAM A DATA DA MARATONA'
print('Checador de Palíndromos do Brasil')
verme = '\033[1;31m'
verde = '\033[1;32m'
branc = '\033[m'
while True:
    try:
        frase = str(input('Frase: ')).strip().upper()
    except ValueError:
        print('Uma frase, tente novamente...')
    else:
        break
f1 = f2 = str()
print(len(frase))
for i in range(len(frase) - 1, -1, -1):  # varre a string do último termo até o termo 0.
    print(len(frase), i)                 # imprime pra testar a lógica do laço for
    if frase[i].isalpha():               # remove os espaços (caracteres não alfanuméricos
        f2 += frase[i]                   # acumula na string 2 a frase invertida sem espaços
for i in range(len(frase)):              # varre a string do primeiro até o último termo
    print(len(frase), i)                 # imprime pra testar a lógica do laço for
    if frase[i].isalpha():
        f1 += frase[i]
print(f1, f2)
print('{} {}É{} um Palíndromo!'.format(frase, verde, branc)) if f1 == f2 else \
    print('{} {}NÃO{} é um Palíndromo.'.format(frase, verme, branc))
# só possívem em phyton
palavras = frase.split()    # dá um split na frase separando nos espaços, ficando só as palavras
junto = ''.join(palavras)   # junta todas as palavras numa string sem os espaços
inverso = junto[::-1]       # associa os volores de junto no inverso começando pelo fim e retrocedendo de 1 em 1
print(junto, inverso)
print('{} {}É{} um Palíndromo!'.format(frase, verde, branc)) if junto == inverso else \
    print('{} {}NÃO{} é um Palíndromo.'.format(frase, verme, branc))
