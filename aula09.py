'''
    ==================================================== Aula 09 =======================================================
                                        Tratamento de cadeia de caractéres (string)
                                            MANIPULAÇÃO DE CADEIAS DE TEXTO
    ====================================================================================================================
'''
'''
                            frase   =  '-C-u-r-s-o- -e-m- -V--í--d--e--o-- --P--y--t--h--o--n--'
                            índice  =    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18  19 20
                
    FATIAMENTO DE STRING
        '[]'            = atribuição de lista porém aqui representará o índice ao fatiar uma string 
                          frase = 'Curso em Vídeo Python'
        - frase[9]      = décida letra = letra 'V' (python diferencia UPPER de LOWER)     
        - frase[9:13]   = [9]=V e [13]=o; Vai do 9 ao 12 (excluí o último índice) Do V ao e = Víde 
                          para incluir o 'o  frase[9:14] = Vídeo
        - frase[9:21]   = funciona pos não consifera o 21 (que não existe), já que para no 20 quando fatia
        - frase[9:21:2] = Do [9] ao [20] pulando de 2 em  >>> V d o P t o.
        - frase[:5]     = Se início omitido ele inicia do caractére 0; Ou seja vai iniciar no índice [0] indo até o 4.
        - frase[15:]    = Indicou início no 15 sem indicar o fim, ou seja, começa no 15 e vai até o fim da string. 
                          15+ = Python
        - frase[9::3]   = Inicia no 9 e vai até o final, pulando de 3 em 3. [(9):():(3)] = V e P h 
    
    Análise
        len(frase)          = comprimento 'lenght' de frase = 21 caractéres = 21
        frase.count('o')    = contar quantas vezes aparece a letra 'o' na string. Ou seja, 3 na string
                              frase.count('o',0,13) faz a contagem já fazendo o fatiamento
        frase.find('deo')   = encontra e mostra onde na string se encontra os caractéres indicados 'deo' no caso. 
                              retorna 11 no caso da string frase (pode trabalhar com uma letra ou várias)
                              frase.find('Android') = Como não existe a função retorna '-1', ou seja, -1 = n tem.
        'Curso' in frase    = Indica se há a palavra 'Curso' dentro de frase, retornando True ou False. Nesse caso True
    
    Transformação
        frase.replace('Python','Android')   =   Procura por 'Python' e substituí por 'Android'. "Curso em Vídeo Android"            
        frase.upper()                       =   Substituí para maiúscula o q não for maiúscula;
        frase.lower()                       =   Substituí para mainúscula o q não for minúscula;
        frase.capitalize()                  =   Joga todos os caracteres pra minúsculo e coloca a primeira letra pra
                                                maiúscula;   
        frase.title()                       =   Joga todo pra minúscula e coloca a primeira letra da CADA PALAVRA para
                                                maiúscula. Formando um título;
        frase.strip()                       =   Remove todos os espaços inúteis no começo e no final da string.
        frase.rstrip()                      =   RIGHT STRIP >>> Trata pela direita, remove apenas os espaços da direita
                                                (no final da string)
        frase.lstrip()                      =   Análogo ao rstrip mas executando na parte esquerda da string (começo)
    
    Divisão     
        frase.split()       =   Divide a string nos espaços ' ', fazendo split em uma LISTA com nova indexação 
        '-'.join(frase)     =   Juntar todos os elementos da LISTA em uma string separados por '-'  

String gigantes quebrando linhas podem ser feitas.
ex.: print(""" asuidasdahsiudhasiuhdasiudashdasuidhasuidashuidasuhd
                asoiuudashipdasghdoasgdasduashduiashdasouidhasuiodas
                asiyuogdfasuiodashdoiuashd asohdasiuhdashdn asoasndnuiasd
                asudhaodas uhasdhu ash asuh dasouhd ashuid ashuiod huas """)
                
frase.upper().count('O') = conta quantos 'O' tem em frase depois de jogar todos os caractéres pra maíusculo  

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])      # pegue o índice [2] de frase splitado (vídeo) e mostre seu índice [3] (e)
>>> e  
'''

# Excercício 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#               *   O nome com todas as letras maiúsculas
#               *   O nome com todas minúsculas
#               *   Quantas letras ao todo (sem considerar espaços)
#               *   Quantas letras tem o primeiro nome

# Excercício 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#                 ex.: Digite um número: 1834
#                      unidade: 4    dezena: 3  centena: 8  milhar: 1

# Excercício 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a nome "Santo".
#

# Excercício 25 - Crie um programa se Leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
#

# Excercício 26 - Faça um programa que leia uma frase pelo teclado e mostre:
#               *   Quantas vezes aparece a letra "A";
#               *   Em que posição aparece a primeira vez;
#               *   Em que posição ela aparece pela última vez.

# Excercício 27 - Faça um programa que leia o nome completo de uma pessoa& mostre em seguida o primeiro e o último nome
#                 separadamente. ex.: Ana Maria Braga Xota Marota >>> Ana Marota.
