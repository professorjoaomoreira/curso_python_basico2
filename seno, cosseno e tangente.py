print ('{:=^90}'.format ('algoritmos para calcular seno cosseno e tangente'))
import math
#print('{:=^90'.format('algoritmos para calcular seno, cosseno e tangente)}'))
angulo = (float(input('Digite o angulo: ')))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(' O seno do ângulo de {:.0f} graus. E o SENO é: {:.2f}'.format(angulo, seno))
print(' O cosseno do ângulo de {:.0f} graus. E o COSSENO é: {:.2f}'.format(angulo, cos))
print(' A tangente do ângulo de {:.0f} graus. E a TANGENTE é: {:.2f}'.format(angulo, tan))
print ('{:=^90}'.format ('Final do programa'))



