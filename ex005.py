# Exercício 5:  Faça um programa que leia um número Inteiro e mostre na tela seu sucessor e seu antecessor.

i = int(input('Número inteiro: '))

# Não existe operador de incremento e decremento em phyton o famoso i++ e i-- etc (causa mto erro de sintaxe)
# Uma maneira que pode ser feita é i += i e i -= i para inc e dec, respectivamente
print('='*8,'Método 1','='*8)
print('Antecessor:\t\t{:=^10} \nNúmero: \t\t{:=^10} \nSucessor: \t\t{:=^10}' .format(i-1, i, i+1))

# Testanto declaração de variáveis em cadeia como em C e utilizando para guardar suc e ant
print('\n'+'='*8,'Método 2','='*8)

s = a = i           # declaração em cadeia funciona
s += 1              # leia-se   s = s + 1
a -= 1              # leia-se   a = a - 1

# Ordem embaralhada apenas para fins de teste. Ordem de print (ant, num, suc) <<< format(num, suc, ant)
print('Antecessor:\t\t{2:^5} \nNúmero: \t\t{0:^5} \nSucessor:\t\t{1:^5}' .format(i, s, a))
