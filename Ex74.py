import random

num = (random.randint(1,10),random.randint(1,10),
       random.randint(1,10),random.randint(1,10),random.randint(1,10))
print(num)
for n in num:
    print(f'{n}', end = ' ')
print(f'\nO maior número sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')