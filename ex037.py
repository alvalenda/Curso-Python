# EXERCÍCIOS  37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversão: >>> 1 para binário >>> 2 para octal e >>> 3 para hexadecimal
print('CONVERSOR DE BASES NUMÉRICAS!!!')
while True:
    try:
        num = int(input('Entre com um número inteiro: '))
    except ValueError:
        print('O valor não é um número inteiro. Tente novamente...')
    else:
        break
"""     Convertendo pra binário na MÃO. Solução bela porém desnecessária 
nums = str
convert = str('')
while True:
    if num > 1:
        convert += str(num % 2)  # concatena num na string - convertendo ele antes
        num = num // 2
    else:
        convert += str(num)
        break
print(convert)

print(''.join(reversed(convert)))  # imprime a string invertida outra forma seria convert[::-1]
print(convert[::-1])  # muito letal isso aí que fiz mas descobri que já existem funções que fazem isso.
"""
print('Digite 1, 2 ou 3 para efetuar a conversão, sendo:')
menu = int(input('1 = Binária\n2 = Octal\n3 = Hexadecimal\n'))
if menu == 1:
    print('{} convertido para base binária é {}'.format(num, bin(num)[2:]))
elif menu == 2:
    print('{} convertido para base octal é {}'.format(num, oct(num)[2:]))
elif menu == 3:
    print('{} convertido para base hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida para o menu de conversão!')
print('\nForte Abraço!!!')  # solução perfeita
