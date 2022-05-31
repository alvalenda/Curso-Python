# EXERCÍCIO 66: Leia vários números inteiros pela teclado. O programa só vai parar quando o user digitar 999, que é
#               a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
contador = soma = int(0)
print('Digite [999] Pra Sair')
while True:
    while True:
        try:
            num = int(input(f'Número {contador + 1}: '))
        except ValueError:
            print('entrada inválida... tente novamente...')
        else:
            break
    if num == 999:
        break
    contador += 1
    soma += num
print(f'Foram digitados {contador} números e a soma deles é {soma}')
