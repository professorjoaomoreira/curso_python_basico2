print('\033[1:31:51:49m{:=^90}'.format('Roleta usando for'))
print('\033[m')
s = 0
for c in range(0,3):
    n = int(input('Digite um valor: '))
    s = s + n
print(s)
print('fim')

print('\033[1:34:51:49m{:.^90}'.format('FINAL DO PROGRAMA'))