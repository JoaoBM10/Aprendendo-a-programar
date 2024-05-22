import random

a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')

Lista = [a1 , a2 , a3 , a4]
random.shuffle(Lista)   #Primeiro embaralhar antes do print.
print('A ordem de apresentação será {}'.format(Lista))
