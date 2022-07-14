n1 = (float(input('Digite a primeira nota: ')))
n2 = (float(input('Digite a segunda nota: ')))
media = (float(n1 + n2)/2)
print('a nota n1 é : {:>10.2f}\n a nota n2 é : {:^10.2f} \ne a  média entre eles é : {:<10.1f}'.format(n1,n2,media))
#ao forçar a media a ter apenas uma casa após a virgula o python já arredonda a nota