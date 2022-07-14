print('{:=^90}'.format('Algoritmos para perguntar o nome:'))
nome = str(input('digite o seu nome: '))
if nome == 'joao':
    print('Nossa! que nome lindo que você tem')
else:
    print('Seu nome é normal!')
print('Bom dia {}'.format(nome))