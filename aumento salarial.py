print('{:=^90}'.format("algoritmo para calcular aumento de salario: "))
salario = (float(input('Informe seu salário: ')))
ajuste = (int(input('informe o aumento em % ')))
aumento = ((ajuste * salario)/100)
print('O valor do seu salário atual é: R${:.2f} mas com o aumento de {}% o salário fica por R${:.2f}'.format(salario, ajuste, (salario + aumento)))

print('{:=^90}'.format('final do programa'))