# EXERCÍCIOS  43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo: >>> abaixo de 18.5: Abaixo do Peso >>> Entre 18.5 e 25: Peso Ideal >>>
# 25 até 30: Sobrepeso >>> 30 até 40: Obesidade >>> Acima de 40: Obesidade mórbida
while True:
    try:
        altura = float(input('Altura em metros: '))
    except ValueError:
        print('Precisa ser um número. Tente novamente.')
    else:
        break
while True:
    try:
        peso = float(input('Peso em Kg: '))
    except ValueError:
        print('Precisa ser um número. tente novamente.')
    else:
        break
imc = peso / (altura ** 2)
if imc >= 40:
    print('IMC {:.2f}\tObesidade de Classe 3 (mórbida). =('.format(imc))
elif imc >= 35:
    print('IMC {:.2f}\tObesidade de Classe 2. =('.format(imc))
elif imc >= 30:
    print('IMC {:.2f}\tObesidade de Classe 1. =('.format(imc))
elif imc >= 25:
    print('IMC {:.2f}\tSobrepeso.'.format(imc))
elif imc >= 18.5:
    print('IMC {:.2f}\tPeso IDEAL!!! =)'.format(imc))
else:
    print('IMC {:.2f}\tAbaixo do peso. =/'.format(imc))
