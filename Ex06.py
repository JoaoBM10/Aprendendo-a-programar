n=int(input('Digite um número:'))
print('O dobro de {} é {}'.format(n,(n*2)))
print('O triplo de {} é {}'.format(n,(n*3)))
print('A raiz quadrada de {} é {:.1f}'.format(n, (n**(1/2))))

#Outro método

n=int(input('Digite um número:'))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de {} é {}.'.format(n,d))
print('O triplo de {} é {}.'.format(n,t))
print('A raiz quadrada de {} é {:.1f}'.format(n,r))