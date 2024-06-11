print('-=-'*10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*10)

import random
from time import sleep

num = int(input('Em que número eu pensei?'))
num2 = random.randint(0,5)
print('Processando...')
sleep(3)
if num == num2:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Erroooooou! Eu pensei no número {} e não no {}'.format(num2 , num))
