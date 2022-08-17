from datetime import date
print('\033[1:34:51:49m{:=^90}'.format(' Analisador completo '))
print('\033[m')#limpa cores
somaidade = 0
maioridade = 0
for pessoa in range(1,3):
    nome = str(input('Informe o nome da {}ª pessoa: '.format(pessoa,'PESSOA'))).strip()
    ano_nasc = int(input('Informe seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano_nasc
    sexo = str(input(('''Escolha a Opção: \n[M] para Masculino\n[F] para Feminino\nQual é sua opção: >> '''))).strip()
    print('----- {}ª PESSOA -----'.format(pessoa))
    print('\nNome: {}\nIdade: {}\nSexo [M/F]: {}'.format(nome,idade,sexo))
    print('----{}ª PESSOA -----'.format(pessoa))

    somaidade = somaidade + idade
    media = somaidade / pessoa
    if pessoa == 1:
        maioridade = idade
    if idade > maioridade:
        maioridade = idade

    print('A soma das idades é: {}, e a media entre estas somas é: {} o total de pessoas è: {}'.format(somaidade, media, pessoa))
    print('A media de idade do grupo é de {} anos'.format(media))
    print('A maior idade é: {}'.format(maioridade))



