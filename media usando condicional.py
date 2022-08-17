print('\033[1:34:51:49m{:=^90}'.format("Calcular a Médias Usando Condionais"))
n1 = float(input("\033[mDgite a nota G1: "))
n2 = float(input("Dgite a nota G2: "))
media = (n1 + n2)
if media >= 7:
    print("A média final é: {}, e o aluno está aprovado".format(media))
elif media < 5:
    print("A média final é: {}, e o aluno está em reprovado sem direito a recuperação ".format(media))
elif media >= 5:
    print('A média final é: {}, o aluno está em recuperação: '.format(media))
else:
    print ('A média final é: {}, o aluno está aprovado! Parabéns...'.format(media))

print('\033[1:31:51:49m{:.^90}'.format('FINAL DO PROGRAMA'))

