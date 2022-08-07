print('\033[1:34:51:49m{:=^90}'.format(' Conversão de Bases Númericas '))
print(('\033[m'), end ='')
#=============================================================
n = int(input('Digite um Número Inteiro: '))
print('o número digitado é: {}'.format(n))

opcao = int(input('''Escolha uma opção :'
[ 1 ] - Digite 1 para binario
[ 2 ] - Digite 2 para octal 
[ 3 ] - Digite 3 para exadecimal: '''))

print("A opcao escolhida foi: {}".format(opcao))

if opcao == 1:
    print('A conversão do nr decimal: {}, em binario é {}'.format(n, bin(n)))
elif opcao == 2:
    print('A  conversaõ do nr decimal: {}, em octadecimal é: {}'.format(n, oct(n)))
elif opcao == 3:
    print('A conversao do nr decimal: {}, em exadecimal é: {}'.format(n, hex(n)))
else:
    print('A opção escolhida é invalida, tente novamente:')




#==============================================================
print('\033[1:31:51:49m{:.^90}'.format(' FINAL DO PROGRAMA '))