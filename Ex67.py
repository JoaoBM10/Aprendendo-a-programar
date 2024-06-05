while True:
    num = int(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        break
    print('--' * 8)
    contador = 0
    while not contador == 10:
        contador += 1
        print(f'{num:<2} x {contador:2} = {num * contador:2}')
    print('--' * 8)
print('Programa de tabuada encerrado! Volte sempre!')

# Utilizando o while com for:

while True:
    num = int(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        break
    print('--' * 8)
    for contador in range(1,11,1):
        print(f'{num:<2} x {contador:2} = {num * contador}')
print('Programa de tabuada encerrado! Volte sempre!')