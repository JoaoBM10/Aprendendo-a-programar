matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
somacoluna = 0
valormaior = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]:'))
        if matriz[linha][coluna] %2 == 0:
            soma += matriz[linha][coluna]
        if coluna == 2:
            somacoluna += matriz[linha][coluna]
        if linha == 1:
            valormaior = matriz[1][0]
        elif valormaior < matriz[1][1]:
            valormaior = matriz[1][1]
        elif valormaior < matriz[1][2]:
            valormaior = matriz[1][2]
print('=-'*20)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end = '')
    print()
print('=-'*20)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {somacoluna}.')
print(f'O maior valor da segunda linha é {valormaior}.')

#Outro método

for linha in range(0,3):
    soma += matriz[linha][2]
# Para somar a terceira coluna

for coluna in range(0,3):
    if coluna == 0:
        valormaior = matriz[1][coluna]
    elif matriz[1][coluna] > valormaior:
        valormaior = matriz[1][coluna]
print(valormaior)
# Para maior valor da segunda linha