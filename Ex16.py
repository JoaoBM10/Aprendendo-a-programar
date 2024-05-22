import math

n = float(input('Digite um número:'))
i = math.trunc(n)
print('O número {} tem a parte Inteira {}.'.format(n , i))

#Outro método

from math import trunc

n = float(input('Digite um número:'))
print('O número {} tem a parte Inteira {}.'.format(n , trunc(n)))

#Outro método

n = float(input('Digite um número:'))
print('O número {} tem a parte Inteira {}.'.format(n , int(n)))
