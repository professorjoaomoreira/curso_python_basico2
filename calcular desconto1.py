print('\033[1:34:51:49m{:=^90}'.format(' Calcular Desconto '))
print('\033[m')#, end='')
val = float(input("Digite um valor em R$: "))
desc = float(input("Digite o Desconto em %: "))
desc1 = val * desc / 100
Tot = val - desc1

print('O valor menos desconto em R$: {:.0f}'.format(Tot))


print('\033[1:31:51:49m{:.^90}'.format(' FINAL DO PROGRAMA '))

