print('\033[1:31:51:49m{:=^90}'.format('Programa para fazer contagem regressiva para fogos de artificio'))
print('\033[m')
import time
sub = 0
for cont in range(10, 0, -1):

    time.sleep(1)
    print(cont)
print('VAI EXPLODIR OS FOGOS')