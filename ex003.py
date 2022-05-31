n1 = input('numero 1: ')
n2 = input('numero 2: ')

n3 = n1 + n2

n4 = float(n1) + float(n2)

# print('n1 = {0} \nn2 = {1} \nn3 = {2} \nn{3} = {4}\n \n' n1, n2, n3, n4, n1 + n2)

print('\n n1 = {}\n n2 = {}\n n1 + n2 = {} (concatena pois o objeto é string)\n n1 + n2 = {} (numérico convertido pra '
      'float)\n'.format(n1, n2, n3, n4))
print('A classe da primeira leitura é: {} \nE a da segunda Leitura é: {}' .format(type(n1), type(n2)))

print('\nOu seja, tudo pode ser refeito setando o tipo primitivo das variáveis na hora de sua leitura/declaração, '
      'vamos testar aqui mesmo e ver a diferença, seu arombáran\n')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o outro: '))
# perceba flavinha arombáran que a variável agora já entra como float na leitura, acabando com o problema
# posso já chamar a soma dentro do print, ou se quiser chamar a leitura como float tb, mas a leitura fica pra próxima

print('\nA soma dos valores {} e {} vale: {}. \nAcertei aronbárannn???' .format(n1, n2, n1+n2))
# agora refazendo a checagem do tipo primitivo da variável
print('\nA classe da Leitura 1 é: {} \nA classe da Leitura 2 é: {}' .format(type(n1), type(n2)))
# para forçar valores inteiros eu poderia ou deveria utilizar int, int seria o recomendado pra amenizar a curva de
# aprendizado