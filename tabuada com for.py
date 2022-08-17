print('\033[1:34:51:49m{:=^90}'.format('faça uma calculadora usando o for'))
print('\033[m')
mult = 0

n = int(input('Digite um numero: '))

for calc in range(1,11):
    mult = mult + calc
    print(n, '*', calc, '=', calc * n)

print('\033[1:31:51:49m{:.^90}'.format('FINAL DO PROGRAMA'))