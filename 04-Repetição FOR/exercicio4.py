#Crie um programa que cadastre alguns produtos e suas quantidades. Primeiro, pergunte quantos produtos o usuário deseja cadastrar. Em seguida, use um laço for para repetir o pedido do nome e da quantidade do produto 
# o número de vezes informado. Durante o laço, mostre na tela cada produto cadastrado no formato: Produto: X | Quantidade: Y

while True:
    numeros_de_produtos = int(input("Quantos produtos você deseja? (limite maximo 10) (ou digite 0 para sair) "))
    if numeros_de_produtos >10:
          print("Numero invalido, tente novamente" "!")
    else:
          break

for pedido in range(numeros_de_produtos):
        nome_produto = input("Digite o nome do produto: ")
        quantidade_de_produtos = int(input("Digite a quantidade (limite maximo 10): "))
        print(f"Produto: {nome_produto} | Quantidade: {quantidade_de_produtos}")
