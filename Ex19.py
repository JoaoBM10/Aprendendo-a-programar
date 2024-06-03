import random

a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')

Lista = [a1 , a2 , a3 , a4]

print(random.choice(Lista))

#Outro método

Escolhindo = random.choice(Lista)
print('O aluno escolhindo foi {}.'.format(Escolhindo))
