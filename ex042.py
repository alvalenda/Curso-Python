# EXERCÍCIOS  42: Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado: >>> Equilátero: (todos os lados iguais) >>> Isósceles: Dois lados iguais >>> Escaleno: Todos os
# lados diferentes
while True:
    try:
        l1 = float(input('Lado um:   '))
        l2 = float(input('Lado dois: '))
        l3 = float(input('Lado três: '))
    except ValueError:
        print('Tem que entrar com \033[1;31mnúmero\033[m irmão... \033[1;31mtente aí de novo.\033[m')
    else:
        break
lista = [l1, l2, l3]
lista.sort()  # Coloca em ordem pra facilitar o teste
if lista[2] < (lista[1] + lista[0]):  # Se testar apenas com o lado maior já satisfaz a condição
    print('Sim! Os segmentos de reta {}, {} e {} podem formar um triângulo.'.format(lista[0], lista[1], lista[2]))
    if      lista[0] != lista[1] != lista[2] != lista[0]:
        print('Trata-se de um triângulo \033[7mESCALENO\033[m.')
    elif    lista[0] == lista[1] == lista[2]:
        print('Trata-se de um triângulo \033[7mEQUILÁTERO\033[m.')
    else:
        print('Trata-se de um triângulo \033[7mISÓSCELES\033[m.')
else:
    print('Não. Infelizmente esses segmentos de reta {}, {} e {} \033[1;31mnão\033[m podem formar um triângulo.' ""
          "".format(lista[0], lista[1], lista[2]))
