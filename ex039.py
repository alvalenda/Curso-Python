# EXERCÍCIOS  39: Faça um programq que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# >>> Se ele ainda vai se alistar ao serviço militar. >>> Se é a hora de se alistar >>> Se já passou o tempo de
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

hoje = datetime.now()
print('{}/{}/{}'.format(hoje.day, hoje.month, hoje.year), hoje.strftime("%A"), end=' -')
print('\t{}:{:02,}.{:02}'.format(hoje.hour, hoje.minute, hoje.second))

while True:
    try:
        nascimento = int(input('Entre com o ano de nascimento: '))
    except ValueError:
        print('Anos são representados por números inteiros, tente novamente...')
    else:
        break

idade = int(hoje.year - nascimento)

if idade == 18:
    print('\nEstá na hora de se alistar, você completa {} anos esse ano.'.format(idade))
elif idade > 18:
    print('\nVocê está atrasado com o compromisso militar há {} ano(s).'.format(idade - 18))
else:
    print('\nVocê deverá se alistar daqui a {} ano(s).'.format(18 - idade))

print('\nTenha um bom dia seu \033[7mFILHA DA PUTA!\033[m')
