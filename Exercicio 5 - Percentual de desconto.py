#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco_mercadoria = input("Digite o preço da mercadoria: ")
desconto = input("Digite o percentual do desconto: ")

valor_desconto = (int(preco_mercadoria) * int(desconto)) /100
valor_total = int(preco_mercadoria) - int(valor_desconto)

print("O valor do desconto é de: R$", valor_desconto, "\nO valor total a pagar com o desconto é de: R$", valor_total)