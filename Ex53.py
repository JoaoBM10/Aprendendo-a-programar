frase = str(input('Digite uma frase:')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
caracteres = len(juntar)
inverso = ''
for intervalo in range(caracteres -1 , -1 , -1):
       inverso += juntar[intervalo]
print(f'o inverso de {juntar} é {inverso}')
if inverso == juntar:
       print('Temos um palídromo!')
else:
       print('A frase digitada não é um palíndromo.')

#Sem utilizar o FOR, utilizando fatiamento
#apagamos o FOR e criamos uma variavel de inverso nova

inverso = juntar[::-1]
print(inverso)