# EXERCÍCIO 48: Programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se
#               encontram no intervalo de 1 até 500.
from time import sleep, perf_counter
tac = perf_counter()
acumula = conta = int(0)
print(acumula)  # imprime 1 como o primeiro múltiplo de 3
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i)
        acumula += i
        conta += 1
        # sleep(0.05)
print(conta, acumula)
tic = perf_counter()
print('\n\nfinalizado em: {}s'.format(tic - tac))
