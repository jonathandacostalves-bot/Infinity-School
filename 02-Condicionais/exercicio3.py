#Crie um programa que peça ao usuário um número inteiro e determine: Se o número é positivo, negativo ou zero. Se o número é par ou ímpar (apenas se for diferente de zero). O programa deve exibir mensagens como: 
# "Número positivo e par" "Número negativo e ímpar" "Número é zero"

numero = int(input("Digite um número: "))

if numero > 0: 
    print("O número é positivo")
    if numero % 2 ==0:
        print("O número é par")
    else:
        print('O número é ímpar')
elif numero < 0:
    print("O número é negativo")
    if numero % 2 != 0:
        print('O número é ímpar.')
    else:
        print('O número é par.')
else:
    print('Zero.')
