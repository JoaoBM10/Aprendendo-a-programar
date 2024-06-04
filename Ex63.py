print('SEQUÊNCIA DE FIBONACCI')
print('=-='*8)

num = int(input('Quantos termos você deseja?'))
contador = 1
fibonacci1 = 0
fibonacci2 = 1

while contador <= num:
    print(f'{fibonacci1} -> ', end = '')
    fibonacci3 = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci3
    contador += 1
print('FIM')