# EXERCÍCIO   35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ele pode ou não
#                 formar um triângulo. (a soma dos dois segmentos tem que ser sempre maior dq o terceiro)
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
lista.sort()  # Coloca em ordem ora facilitar o teste
if lista[2] < (lista[1] + lista[0]):  # Se testar apenas com o lado maior já satisfaz a condição
    print('Sim! Os segmentos de reta {}, {} e {} podem formar um triângulo.'.format(lista[0], lista[1], lista[2]))
else:
    print('Não. Infelizmente esses segmentos de reta {}, {} e {} \033[1;31mnão\033[m podem formar um triângulo.' ""
          "".format(lista[0], lista[1], lista[2]))
