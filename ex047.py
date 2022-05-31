# EXERCÍCIO 47: Programa Programa que mestre na tela todos os números PARES no intervalo en 1 e 50
#
from time import sleep
for i in range(51):  # ou range(2, 51, 2): e remova o if após a função print(i)
    print(i) if i % 2 == 0 else ()
    sleep(0.05)
# for i in range(2, 51, 2):
#     print(i)
#     sleep(0.05)
