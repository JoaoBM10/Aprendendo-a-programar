s = 0
for intervalo in range(1, 7, 1):
    num = int(input('Digite um número inteiro:'))
    if num %2 == 0:
        s += num
print(f'A soma dos números inteiros pares é {s}')       