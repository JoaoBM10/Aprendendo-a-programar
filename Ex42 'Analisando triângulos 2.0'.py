print('-=' * 13)
print('Analisador de triângulos')
print('-=' * 13)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os segmentos acima PODEM formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo formado é o Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado é o Isósteceles.')
    else:
        print('O triângulo formado é o Escaleno.')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')

