#Crie um sistema que ajude um caixa de loja a registrar vendas até que o cliente finalize a compra: Pergunte ao usuário o preço de cada item. Use um loop while para continuar somando os valores enquanto o usuário
#  não digitar 0, que indica o fim da compra. Após o término, exiba o total da compra no formato: "Total da compra: R$ X". A cada item adicionado, exiba também o valor acumulado até o momento. Dica: use uma variável 
# para acumular o total e outra para armazenar o valor do item informado pelo usuário.

valor_total_da_compra = 0
while True:
    soma = float(input("Digite o valor dos itens (Digite 0 para finalizar): "))    

    if soma ==0:
        print(f"O valor total dos itens é R${valor_total_da_compra}")
        break
    else:
        valor_total_da_compra +=soma
        print(f"Valor total até o momento R${valor_total_da_compra}")

        