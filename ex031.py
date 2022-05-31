# EXERCÍCIO   31: Desenvolva um programa que pergunta a distância de uma viagem em KM, calcule o preço da passagem,
#                 cobrando R$0,50 / Km para viagens até 200Km e R$0,45 para viagens mais longas.
print('\033[1;36;41m-=*=-'*6+'\033[1;32;41m{ INTERBUS BRASIL!!!}'+'\033[1;39;41m-=*=-\033[m'*6)
print('\t\t\t\t\t\t\t\t \033[7mBom Dia!!!\033[m')

while True:                     # adorei esse bloco pra testar entrada. Vou usar sempre.
    try:
        dist = float(input('Qual a distância(em KM) da viagem? '))
    except ValueError:
        print('Entrada inválida! Entre com um valor numérico...')
    else:
        break

if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45

print('O valor da passagem para o destino selecionado é de: R${:10,.2f}' .format(preco))
print('BOA VIAGEM!!!!')
