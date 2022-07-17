print('{:=^90}'.format('perguntar o valor de um salario se maior de 1250, aplicar 15%. salarios menores 10%'))
salario = float(input('Informe qual o seu salário: '))
dez = int(salario * 10/100)
quinze = int(salario * 15/100)
if salario >= 1250:
    print('O seu salário é R${:.2f} e vai receber um aumento de 10% e o valor vai ser de: R${:.2f}\n'
          'O valor final a receber vai ser de R${:.2f} '.format(salario, dez, salario + dez))
else:
    print('O seu salário é R${:.2f} e vai receber um aumento de 15% e o valor vai ser de: R${:.2f}\n'
          'O valor final a receber vai ser de R${:.2f} '.format(salario, quinze, salario + quinze))