print('{:=^90}'.format('Algoritmos para fazer, maiuscula, minuscula e contar o numero de letras'))
nome = str(input('Digite seu nome completo: '))
print(('seu nome em  maiusculo é: ',nome.upper()))
print(('seu nome com as primeiras letras em  maiusculo é :',nome.title()))
print(' A contagem de letras em seu nome completo  é:',nome.count(''),'letras.')
dividido = (nome.split())
print(' O seu primeiro nome é: ',dividido[0],' e o número de letras em é: ',dividido[0].count(''), 'letras.')
print(nome[::2])
print(nome.count('o'))
print(len(nome.lstrip()))
print(len(nome.rstrip()))
print(nome.replace('joao','pedro'))



