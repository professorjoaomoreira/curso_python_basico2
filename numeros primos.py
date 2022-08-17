print('\033[1:34:51:49m{:=^90}'.format('leia um numero inteiro e diga se ele é primo'))
print('\033[m')
tot = 0
num = int(input('digite um numero: '))
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[34m',end=' ')
        tot = tot + 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')

print('\n\033[mO número {} foi divisivel  {} vezes'.format(num, tot))
if tot == 2:
    print('é por isso ele é primo')
else:
    print('é por isso que ele não é primo')

