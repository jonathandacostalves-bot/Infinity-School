#Projeto Prático Crie um programa em Python que interaja com o usuário para coletar dados pessoais (nome, idade, cidade), calcular o IMC (com peso e altura informados), e informar se a pessoa está com peso 
#ideal ou não. O programa deve usar os conceitos de variáveis, tipos e entrada/saída. Requisitos: Pedir ao usuário o nome, idade, cidade, peso e altura. Calcular o IMC = peso / (altura * altura) 
#Mostrar uma mensagem de boas-vindas com o nome e cidade. Mostrar a idade do usuário. Mostrar o valor do IMC com 2 casas decimais. Tratar entradas para garantir que peso e altura sejam números válidos.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite o nome da sua cidade: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura * altura)

print(f"""
    Seja bem vindo {nome} a cidade de {cidade}
    Você tem {idade} anos e está com o valor do IMC {IMC:.2f}""")
    