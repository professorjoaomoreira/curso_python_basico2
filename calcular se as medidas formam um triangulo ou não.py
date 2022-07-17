print('\033[0:22:41m\{:=^90}'.format('ver as somas de dois lados para ver se forma triangulo ou não'))
ret1 =int(input('\033[m\digite o valor da primeira reta: '))
ret2 = int(input('digite o valor da segunda reta: '))
ret3 = int(input('digite o valor da terceira reta: '))
#tri = (ret1 + ret2)

if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:
    print('Com os valores {}, {} e {}, é possivel formar um triângulo'.format(ret1, ret2, ret3))
else:
    print('Com os seguintes valores: {}, {} e {} não é possivel formar um triângulo'.format(ret1, ret2, ret3))

print('\033[30:42m{:.^90}'.format('FINAL DO PROGRAMA'))
