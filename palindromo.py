frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
'''outra maneira de fazer é usando o fatiamento inverso = junto [::-1]'''
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos palindromo')
else:
    print('A frase digitada não é um palindromo')

'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print("")
if inverso == junto:
    print('Temos um palíndromo!')
else:
print('Você digitou a frase {}'.format(junto))'''
