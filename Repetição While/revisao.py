#Tabuada com Condicional: Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10), mas apenas para os resultados que forem múltiplos de 3.

contador = 1
numero = int(input("Digite um número: "))
multiplicacao = 0
while contador <= 10:
    multiplicacao = numero * contador
    contador +=1
    if multiplicacao % 3 ==0:
        print(f"O valor é {multiplicacao}")