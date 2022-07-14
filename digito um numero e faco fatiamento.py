print('{:=^90}'.format('digitar um numero depois fatiar unidade, dezena, centena e milhar'))
num = int(input('Digite um número entre 0 e 9999: '))
n = (str(num))
print('O número digitado      é: {} '.format(num))
print('A unidade do número {} é: {}'.format(num, n[3]))
print('A dezena do número  {} é: {}'.format(num, n[2]))
print('A centena do número {} é: {}'.format(num, n[1]))
print('O milhar do número: {} é: {}'.format(num, n[0]))


print('{:=^90}'.format('FINAL DO PROGRAMA'))
