import math

a = float(input('Digite o valor do ângulo:'))
rad = math.radians(a)
sen = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)
print('O valor de seno é {:.2f}.'.format(sen))
print('O valor de cosseno é {:.2f}.'.format(cos))
print('O valor da tangente é {:.2f}.'.format(tg))