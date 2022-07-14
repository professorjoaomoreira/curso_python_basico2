#desenvolva um algoritmo que leia um númer
#mostre o seu dobro, triplo e raiz quadrada
import math
n = (float(input('Digite um número: ')))
dobro = n * 2
triplo = n * 3
raiz = math.pow(n, 1/2)
raiz1 = pow(n,1/2)
print ('O número digitado é:',n,'o dobro é: ',dobro, 'o triplo é: ',triplo)
print ('O número digitado é: {}, o seu dobro é: {}, o triplo é: {} e sua raiz quadrada é: {} '.format(n,dobro,triplo, raiz))
print ('outra maneira de calcular a raiz de n é: {}'.format(raiz1))

