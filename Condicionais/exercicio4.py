#Verificar Status de Taxa de Desconto: Crie um programa que peça ao usuário o preço original de um produto e a quantidade comprada. Use if para verificar se a quantidade é maior que 10 para aplicar um desconto de
#  10% sobre o total.

preco = float(input("Digite o valor do produto: "))
quantidades = int(input("Quantos produtos você comprou?: "))
precofinal = preco * quantidades 
desconto = precofinal * 0.9

if quantidades >=10:
    print(f"Você comprou {quantidades} quantidades e deu o valor total de {precofinal}R$ e ganhou 10% desconto sendo {desconto:.2f}R$ de desconto" "!")
else:
    print(f"Você não tem direito ao desconto devido ter comprado somente {quantidades} quantidades")

#Sistema de Login Simples: Desenvolva um programa que peça ao usuário um nome de usuário e uma senha e use if para verificar se são iguais a "admin" e "1234", respectivamente.

usuario = input("Digite o seu login: ")
senha = int(input("Digite sua senha: "))

if usuario == "admin" and senha == int("1234"):
    print("Acesso liberado")
else:
    print("Acesso negado")
