n1 = float(input('Primeiro valor:'))
n2 = float(input('Segundo valor:'))
n3 = float(input('Terceiro valor:'))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
