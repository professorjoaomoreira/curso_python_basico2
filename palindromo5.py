frase = str(input('dite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]

if inverso == junto:
    print('A frase {} se inverte em {} e forma um palindromo'.format(frase, inverso))
else:
    print('A frase {} se inverte em {} e não forma um palindromo'.format(frase, inverso))
