n = float(input('Digite um valor em Metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A conversão de metros para quilometros é {}, em hm é: {}, em decimetros é:{}.'.format(km, hm, dm))
print ('A conversão do valor informado em centimetros é: {:0f}, em decimetro é: {:0f} e em centimetros é: {:0f}'.format(cm, dm, mm))
