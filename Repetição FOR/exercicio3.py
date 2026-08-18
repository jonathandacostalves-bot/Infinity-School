#Crie um programa que peça ao usuário uma palavra e, usando um loop for, conte quantas vogais existem nessa palavra. Ao final, exiba a quantidade total de vogais encontradas.

palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
vogais_encontradas = ""
quantidade_vogais = 0

for letras in palavra:
    if letras in vogais:
        vogais_encontradas += letras
        quantidade_vogais += 1