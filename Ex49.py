num = int(input('Digite um número para saber sua tabuada:'))
print('='*20)
for multiplicador in range(0 , 11 , 1):
    tabuada = num * multiplicador
    print(f'{num:<2} x {multiplicador:2} = {tabuada}')
print('='*20)

#Sem a variavel tabuada ficaria:

num = int(input('Digite um número para saber sua tabuada:'))
for multiplicador in range(0 , 11 , 1):
    print(f'{num:<2} x {multiplicador:2} = {num*multiplicador}')