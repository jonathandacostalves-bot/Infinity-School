
#Crie um programa que solicite ao usuário: Idade da pessoa Se possui carteira de motorista (True ou False) O programa deve verificar se a pessoa pode dirigir. Para isso, a pessoa precisa ter 18 anos ou mais e ter 
# carteira. Exiba na tela: "Pode dirigir" se a pessoa atender aos critérios "Não pode dirigir" caso contrário Dica: use os operadores >= e and.

idade = int(input("Digite sua idade: "))
carteira = input("Você tem carteira de motorista: ")

if idade >= 18 and carteira == 'sim':
    print(f"Você possui {idade} anos e tem carteira e pode dirigir")
elif idade >= 18 and carteira == 'nao':
    print(f"Você possui {idade} anos mas não tem carteira e não pode dirigir")
else:
    print("Você não pode dirigir")

