print('\033[0:22:41m\{:=^90}'.format('usando if, elif, else: '))
nome =str(input('\033[m\'''Digite um nome? '))
if nome == 'Gustavo':
    print('Que nome lindo')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print ('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia, Jessica, Juliana':
    print('Belo nome feminino. ')
else:
    print('Seu nome é bem normal.')
print(' Tenha um bom dia, {}!'.format(nome.upper()))


print('\033[30:42m{:.^90}'.format('FINAL DO PROGRAMA'))

#cores = {'limpa':'\033[m',
#         'azul':'\033[34m',
#         'amarelo':'\033[33m',
#         'preto e branco':'\033[7;30'}
