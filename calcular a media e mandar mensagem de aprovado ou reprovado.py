print('{:=^90}'.format('Algoritmo para calcular a média usando condicionais'))
n1 = float(input('digite a nota do n1: '))
n2 = float(input('digite a nota do n2: '))
media = (n1 + n2) / 2
#print('A média foi: {:.2f}'.format(media))

if media >= 6.0:
    print ('Parabens você foi aprovado e sua média final é: {:.2f}'.format(media))
else:
    print ('estude mais sua média final é: {:.2f} '.format(media))

print('{:=^90}'.format('Formato simplificado de fazer a mesma coisa'))
print('parabens! sua média é: {:.2f}'.format(media) if media >=6 else 'estude mais! sua média é: {:.2f}'.format(media))


print('{:.^90}'.format('FINAL DO PROGRAMA'))
