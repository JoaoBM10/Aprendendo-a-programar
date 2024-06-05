contador = num = soma = 0

while True:
    num = int(input('Digite um valor (1000 para parar):'))
    if num == 1000:
        break
    contador += 1
    soma += num
print(f'A soma dps {contador} números foi {soma}.')