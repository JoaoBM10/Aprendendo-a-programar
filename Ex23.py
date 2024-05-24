#Funciona, mas só com números de quatro digitos.

num = int(input('Informe um número:'))
n = str(num)
print('Analisando o número {}:'.format(n))
print('Unidade:{}'.format(n[3]))
print('Dezena:{}'.format(n[2]))
print('Centena:{}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

#Método matemático

num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}:'.format(n))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar: {}'.format(m))

#Outro método

n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhares.'.format(n, n2[1]))
print('O número {} possui, {} centenas. '.format(n, n2[2]))
print('O número {} possui, {} dezenas. '.format(n, n2[3]))
print('O número {} possui, {} unidades.'.format(n, n2[4]))