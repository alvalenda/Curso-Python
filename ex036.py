# EXERCÍCIOS  36: Crie um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e sem quantos anos ele vai pagar.Calcule o valor da
# prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empr será negado.
print('\033[7mCREDFLA - EMPRÉSTIMOS CONSIGNADOS\033[m')
while True:  # leitura e teste da variável casa
    try:
        casa = float(input('Valor do Imóvel em R$: '))
    except ValueError:
        print('O valor do imóvel precisa ser um número. Tente novamente')
    else:
        break
while True:  # leitura e testa da variável renda
    try:
        renda = float(input('Renda mensal do consignatário em R$: '))
    except ValueError:
        print('A renda precisa ser um número. Tente novamente')
    else:
        break
while True:  # leitura e teste da variável tempo
    try:
        tempo = int(input('Tempo para quitação em ANOS: '))
    except ValueError:
        print('O tempo precisa ser um número INTEIRO. Tente novamente')
    else:
        break
# print(casa, renda, tempo)
mensal = casa / (tempo * 12)
limite = renda * 0.3

if mensal <= limite:
    print('\033[7mCrédito Aprovado!!!\033[m')
    print('Valor da Prestação:\tR${:8,.2f}'.format(mensal))
    print('Número de Parcelas:\t  {:4}'.format(tempo))
else:
    print('\033[7mCrédito REPROVADO!!!\033[m\nPrestação acima do valor limite de R${:8,.2f}'.format(limite))
