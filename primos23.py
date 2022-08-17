tot = 0

num = int(input('digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        tot = tot + 1
        if tot == 2:
            print('')
        else:
            print('')
print('O numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E é por isso que ele é primo')
else:
    print('Esse número não é primo')





