#Crie um programa que solicite ao usuário a entrada de 5 números inteiros. Utilize um contador para controlar quantas vezes o loop foi executado. Utilize um acumulador para somar os números digitados. Ao final, 
# calcule e exiba a média dos números.

contador = 0
soma = 0
while contador <5:
    numero = int(input("Digite um número: "))
    soma+= numero
    contador +=1
    media = soma / contador
print(f"A média é {media}")