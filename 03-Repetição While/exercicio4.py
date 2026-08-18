#Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.

contador = 1
soma = 0

while contador <= 100:
    if contador % 2 == 0:
        soma += contador
    contador += 1
print(f"A soma é {soma}")