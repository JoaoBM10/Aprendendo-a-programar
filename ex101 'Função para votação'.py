from datetime import date
#O ideal é fazer o import dentro da função pra economia de memoria, 
#pois só será utilizado na função e não no programa todo.

def voto(ano):
    atual = date.today(). year
    idade = atual - ano
    print(f'A idade é de {idade} anos.')
    if idade < 16:
        return 'O voto é NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return 'O voto é OPCIONAL.'
    else:
        return 'O voto é OBRIGATÓRIO.'
    

nascimento = int(input('Data de nascimento:'))
print(voto(nascimento))